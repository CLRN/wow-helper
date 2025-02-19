from statemachine import StateMachine, State
from algos.relativity import Relativity
from components.settings import Settings
from components.path_tracker import PathTracker
from machines.rotation import Rotation
from machines.looting import MobLooting
from machines.mob_search import MobSearch
from machines.combat_action import CombatAction
from machines.moving import Moving
from memory.camera import world_to_screen
from PIL import Image, ImageDraw

import logging
import time
import pyautogui
import os
import shutil
import math


class MobFarmer(StateMachine):
    searching = State('Searching for next mob')
    fighting = State('Fighting with mob')
    looting = State('Looting mobs')
    restoring = State('Restoring HP/Power', initial=True)
    eating = State('Eating/drinking to restore HP/Power')
    fleeing = State('Running away from mobs')

    found = searching.to(fighting)
    lost = fighting.to(searching)
    killed = fighting.to(restoring)
    restored = eating.to(looting) | restoring.to(looting)
    looted = looting.to(searching)
    eat = restoring.to(eating)
    fight = searching.to(fighting) | restoring.to(fighting) | looting.to(fighting)
    loot = searching.to(looting)
    flee = fighting.to(fleeing)
    fled = fleeing.to(restoring)

    def __init__(self, window, controller, object_manager, combat_model, mob_picker, telegram_bot):
        self.window = window
        self.controller = controller
        self.object_manager = object_manager
        self.combat_model = combat_model
        self.telegram_bot = telegram_bot

        self.mob_picker = mob_picker
        self.rotation_machine = Rotation(controller)
        self.moving_machine = Moving(controller)
        self.looting_machine = MobLooting(self.controller, self.rotation_machine, self.moving_machine)
        self.searching_machine = MobSearch(self.controller, self.rotation_machine, self.moving_machine)
        self.fighting_machine = CombatAction(self.controller, self.rotation_machine, self.moving_machine)

        self.fighting_mobs = None
        self.transition_time = time.time()
        self.last_report_time = 0
        self.last_attack_target = None
        self.attack_start_time = 0
        self.attack_start_hp = 0
        self.last_incoming_dps_time = 0

        self.loot_target_tracker = PathTracker(None, [], Settings.LOOTING_RANGE)
        self.attack_target_tracker = PathTracker(None, [], Settings.SEARCH_RANGE)
        self.fight_target_tracker = PathTracker(None, [], Settings.SEARCH_RANGE)

        self.last_target_path = list()

        StateMachine.__init__(self)

        if os.path.exists('screens'):
            shutil.rmtree('screens')
        os.makedirs('screens')

    def _update_paths(self):
        self.attack_target_tracker.target, self.attack_target_tracker.path = \
            self.mob_picker.pick_alive(self.moving_machine.is_sticking)
        self.loot_target_tracker.target, self.loot_target_tracker.path = \
            self.mob_picker.pick_lootable(self.moving_machine.is_sticking)

    def _attack_or_loot(self):
        distance_to_loot = Relativity.distance(self.object_manager.player(), self.loot_target_tracker.target) \
            if self.loot_target_tracker.target else 9999
        closest = self.mob_picker.pick_closest()

        if not self.loot_target_tracker.target or closest and \
                Relativity.distance(self.object_manager.player(), closest) < distance_to_loot:
            return True, False
        else:
            return False, True

    def _report(self, force=False):
        if not force and time.time() - self.last_report_time < Settings.REPORTING_TIME:
            return

        self.last_report_time = time.time()

        rect = self.window.rect()
        screen = pyautogui.screenshot(region=(rect.left_top[0],
                                              rect.left_top[1],
                                              rect.bottom_right[0] - rect.left_top[0],
                                              rect.bottom_right[1] - rect.left_top[1]))

        name = f'./screens/{int(time.time())}.jpg'
        screen.save(name)

        player = self.object_manager.player()
        target = self.attack_target_tracker.target

        if target:
            coords = list()

            im = Image.open(name)
            d = ImageDraw.Draw(im)

            for point in [player] + self.attack_target_tracker.path + [target]:
                on_screen = self._get_coords(point)
                if on_screen:
                    x = on_screen[0] - rect.left_top[0]
                    y = on_screen[1] - rect.left_top[1]
                    coords.append((x, y))

            line_color = (0, 0, 255)
            d.line(coords, fill=line_color, width=2)
            im.save(name)

        logging.info(f"{self.current_state_value}, player: {player}, target: {player.target()}, "
                     f"mobs: {self.fighting_mobs}")

        self.telegram_bot.new_status(f"{self.current_state_value}, hp: {player.hp()}/{player.max_hp()}, "
                                     f"mobs: {len(self.fighting_mobs or [])},", name)

    def _get_coords(self, unit):
        return world_to_screen(self.object_manager.process, self.window, unit.x(), unit.y(), unit.z())

    def _do_searching(self):
        buf_to_cast = self.combat_model.get_next_buff()
        if buf_to_cast:
            self.controller.press(buf_to_cast.bind_key)
            return

        to_attack, to_loot = self._attack_or_loot()
        if to_loot:
            self.loot()
            return

        target, required_range = self.attack_target_tracker.next(self.object_manager.player())

        if not target:
            self._update_paths()
            return

        if not self.last_attack_target or self.last_attack_target.id() != target.id():
            self.last_attack_target = target
            logging.info(f"Switching attack target from {self.last_attack_target} to: {target}")
            self._report(force=True)

        if self.searching_machine.process(player=self.object_manager.player(),
                                          found_mob=target,
                                          target=self.object_manager.target(),
                                          target_coords=self._get_coords(target),
                                          required_range=required_range):
            self.found()

    def _do_fighting(self):
        target = self.object_manager.target()
        if not target or not target.hp():
            if not len(self.fighting_mobs):
                self.killed()
                return
            else:
                target = self.fighting_mobs[0]

        if not len(self.last_target_path) and (self.object_manager.target() or self.moving_machine.is_sticking):
            self.fight_target_tracker.target, self.fight_target_tracker.path =\
                self.mob_picker.path_to_target(self.moving_machine.is_sticking)

        player = self.object_manager.player()
        if player.hp() == player.max_hp():
            self.attack_start_time = time.time()
            self.attack_start_hp = player.hp()

        diff = time.time() - self.attack_start_time
        incoming_dps = (math.fabs(self.attack_start_hp - player.hp()) / diff) if diff > 1 else 0
        to_die = (player.hp() / incoming_dps) if incoming_dps else 9999
        if time.time() - self.last_incoming_dps_time > 5:
            logging.info(f"Incoming DPS: {incoming_dps}, to die: {to_die}, mobs: {len(self.fighting_mobs)}")
            self.last_incoming_dps_time = time.time()

        if self.combat_model.get_need_to_flee(self.fighting_mobs) or (incoming_dps > 0 and to_die < Settings.FLEE_SECONDS_TO_DIE_THRESHOLD):
            logging.info(f"Running away from {self.fighting_mobs}, "
                         f"incoming DPS: {incoming_dps}, to die: {to_die}, player: {self.object_manager.player()}")
            self.flee()
            return

        spell = self.combat_model.get_next_attacking_spell(self.fighting_mobs, target)
        self.fight_target_tracker.required_range = spell.max_range
        next_target, required_range = self.fight_target_tracker.next(player)

        self.fighting_machine.process(player=player,
                                      target=next_target,
                                      next_spell=spell,
                                      is_casting=player.spell(),
                                      required_range=required_range)

    def _do_restoring(self):
        # TODO: move to a separate state machine
        player = self.object_manager.player()
        if player.hp_percent() > Settings.REGEN_HP_THRESHOLD and player.power_percent() > Settings.REGEN_POWER_THRESHOLD:
            self.restored()
        elif player.hp_percent() < Settings.REGEN_HP_THRESHOLD and player.power_percent() > Settings.REGEN_POWER_THRESHOLD:
            spell = self.combat_model.get_healing_spell()
            if spell and not player.spell():
                # logging.info(f"Healing with {spell.bind_key}, player: {player}")
                self.controller.press(spell.bind_key)
        else:
            spell = self.combat_model.get_next_power_regen_spell()
            if spell and spell.bind_key and not player.spell():
                self.controller.press('x')
                self.controller.press(spell.bind_key)
                self.eat()

    def _do_eating(self):
        player = self.object_manager.player()
        if player.hp() == player.max_hp() and player.power() == player.max_power():
            self.restored()

    def _do_looting(self):
        if time.time() - self.transition_time < Settings.LOOT_ACTION_DELAY_SECONDS:
            return

        player = self.object_manager.player()
        if player.spell():
            return  # already looting

        to_attack, _ = self._attack_or_loot()
        is_loot_good = self.loot_target_tracker.target and \
                       (self.loot_target_tracker.target.loot() or self.loot_target_tracker.target.skin()) and \
                       self.object_manager.has_object(self.loot_target_tracker.target.id())
        if to_attack or not is_loot_good or player.hp_percent() < Settings.REGEN_HP_THRESHOLD:
            self.looted()
            return

        target, required_range = self.loot_target_tracker.next(self.object_manager.player())

        self.looting_machine.process(player=player,
                                     target=target,
                                     target_coords=self._get_coords(target),
                                     required_range=required_range)

    def _do_fleeing(self):
        if not len(self.fighting_mobs):
            self.fled()
            return

        angle = Relativity.angle(self.object_manager.player(), self.fighting_mobs[0])
        self.rotation_machine.process(angle, Settings.FLEE_ANGLE_RANGE)

        # TODO: calculate fleeing path
        self.moving_machine.process(self.object_manager.player(), self.fighting_mobs[0], 100, [])

        spell = self.combat_model.get_next_fleeing_spell()
        if spell and spell.bind_key:
            self.controller.press(spell.bind_key)

    def process(self):
        assert self.object_manager.player().hp()  # crash it when dead for now

        self.fighting_mobs = self.mob_picker.fighting_mobs()
        self._report()
        if len(self.fighting_mobs) and not self.is_fighting and not self.is_fleeing:
            self.fight()
        else:
            getattr(self, f"_do_{self.current_state_value}")()

    def on_enter_searching(self):
        logging.info("Searching")
        self._update_paths()
        self.transition_time = time.time()

    def on_enter_fighting(self):
        logging.info(f"Fighting: {self.object_manager.objects()}")
        self._update_paths()
        self.transition_time = time.time()
        self.attack_start_time = time.time()
        self.attack_start_hp = self.object_manager.player().hp()
        self.last_target_path = list()

    def on_enter_restoring(self):
        logging.info("Restoring")
        self.transition_time = time.time()

    def on_enter_eating(self):
        logging.info("Eating")
        self.transition_time = time.time()

    def on_enter_looting(self):
        self._update_paths()
        logging.info("Looting")
        self.transition_time = time.time()

    def on_enter_fleeing(self):
        logging.info("Fleeing")
        self.rotation_machine.is_kiting = True
        self.moving_machine.is_kiting = True

    def on_exit_fighting(self):
        self.fighting_machine.stop()

    def on_exit_fleeing(self):
        self.rotation_machine.is_kiting = False
        self.moving_machine.is_kiting = False
