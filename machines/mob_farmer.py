from statemachine import StateMachine, State
from algos.relativity import Relativity
from components.settings import Settings
from machines.rotation import Rotation
from machines.looting import MobLooting
from machines.mob_search import MobSearch
from machines.combat_action import CombatAction
from memory.camera import world_to_screen

import logging
import time
import pyautogui
import os
import shutil


class MobFarmer(StateMachine):
    searching = State('Searching for next mob')
    fighting = State('Fighting with mob')
    looting = State('Looting mobs')
    restoring = State('Restoring HP/Power', initial=True)
    eating = State('Eating/drinking to restore HP/Power')

    found = searching.to(fighting)
    lost = fighting.to(searching)
    killed = fighting.to(restoring)
    restored = eating.to(looting) | restoring.to(looting)
    looted = looting.to(searching)
    eat = restoring.to(eating)
    fight = searching.to(fighting) | restoring.to(fighting) | looting.to(fighting)
    loot = searching.to(looting)

    def __init__(self, window, controller, object_manager, combat_model, mob_picker, telegram_bot):
        self.window = window
        self.controller = controller
        self.object_manager = object_manager
        self.combat_model = combat_model
        self.telegram_bot = telegram_bot

        self.mob_picker = mob_picker
        self.rotation = Rotation(controller)
        self.looting_machine = MobLooting(self.controller, self.rotation)
        self.searching_machine = MobSearch(self.controller, self.rotation)
        self.fighting_machine = CombatAction(self.controller, self.rotation)

        self.fighting_mobs = None
        self.transition_time = time.time()
        self.last_report_time = 0

        StateMachine.__init__(self)

        if os.path.exists('screens'):
            shutil.rmtree('screens')
        os.makedirs('screens')

    def _pick_attack_or_loot(self):
        loot = self.mob_picker.pick_lootable()
        distance_to_loot = Relativity.distance(self.object_manager.player(), loot) if loot else 9999
        closest = self.mob_picker.pick_closest()
        target = self.mob_picker.pick_alive()

        if closest and Relativity.distance(self.object_manager.player(), closest) < distance_to_loot:
            loot = None
        else:
            target = None
        return target, loot

    def _report(self):
        if time.time() - self.last_report_time < Settings.REPORTING_TIME:
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
        logging.info(f"{self.current_state_value}, player: {player}, target: {player.target()}, "
                     f"mobs: {self.fighting_mobs}")

        self.telegram_bot.new_status(f"{self.current_state_value}, hp: {player.hp()}/{player.max_hp()}, "
                                     f"mobs: {len(self.fighting_mobs or [])},", name)

    def _get_coords(self, unit):
        return world_to_screen(self.object_manager.process, self.window, unit.x(), unit.y(), unit.z())

    def _do_searching(self):
        attack, loot = self._pick_attack_or_loot()
        if not attack and loot:
            self.loot()
            return

        if not attack:
            return

        buf_to_cast = self.combat_model.get_next_buff()
        if buf_to_cast:
            self.controller.press(buf_to_cast.bind_key)
            return

        distance = Relativity.distance(self.object_manager.player(), attack)
        target = self.object_manager.target()

        angle = Relativity.angle(self.object_manager.player(), attack)
        if self.searching_machine.active(distance,
                              target.id() == attack.id() if target else False,
                                         self._get_coords(attack),
                                         angle):
            self.found()

    def _do_fighting(self):
        target = self.object_manager.target()
        if not target or not target.hp():
            if not len(self.fighting_mobs):
                self.killed()
                return
            else:
                target = self.fighting_mobs[0]

        # if len(self.fighting_mobs) and target and target not in self.fighting_mobs:
        #     self.controller.press('esc')
        #     time.sleep(1)  # TODO: remove sleep
        #     return

        player = self.object_manager.player()
        self.fighting_machine.active(Relativity.distance(player, target),
                                     Relativity.angle(self.object_manager.player(), target),
                                     self.combat_model.get_next_attacking_spell(self.fighting_mobs, target),
                                     player.spell())

    def _do_restoring(self):
        # TODO: move to a separate state machine
        player = self.object_manager.player()
        if (player.hp() * 100) / player.max_hp() > Settings.REGEN_HP_THRESHOLD and \
           (player.power() * 100) / player.max_power() > Settings.REGEN_POWER_THRESHOLD:
            self.restored()
        elif (player.hp() * 100) / player.max_hp() < Settings.REGEN_HP_THRESHOLD and \
             (player.power() * 100) / player.max_power() > Settings.REGEN_POWER_THRESHOLD:
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
        attack, loot = self._pick_attack_or_loot()
        if attack and loot:
            self.looted()
            return

        if time.time() - self.transition_time < Settings.LOOT_ACTION_DELAY_SECONDS:
            return

        player = self.object_manager.player()
        if not loot and time.time() - self.looting_machine.last_looting_time > Settings.LOOT_ACTION_DELAY_SECONDS or \
           (player.hp() * 100) / player.max_hp() < Settings.REGEN_HP_THRESHOLD:
            self.looted()
        elif loot:
            distance = Relativity.distance(self.object_manager.player(), loot)
            angle = Relativity.angle(self.object_manager.player(), loot)
            self.looting_machine.active(distance, self._get_coords(loot), angle)

    def process(self):
        assert self.object_manager.player().hp()  # crash it when dead for now

        self.fighting_mobs = self.mob_picker.fighting()
        self._report()
        if len(self.fighting_mobs) and not self.is_fighting:
            self.fight()
        else:
            for phase in ['looting', 'searching', 'fighting']:
                if phase != self.current_state_value:
                    getattr(self, f"{phase}_machine").inactive()

            getattr(self, f"_do_{self.current_state_value}")()

    def on_enter_searching(self):
        logging.info("Searching")
        self.transition_time = time.time()

    def on_enter_fighting(self):
        logging.info(f"Fighting: {self.object_manager.objects()}")
        self.transition_time = time.time()

    def on_enter_restoring(self):
        logging.info("Restoring")
        self.transition_time = time.time()

    def on_enter_eating(self):
        logging.info("Eating")
        self.transition_time = time.time()

    def on_enter_looting(self):
        logging.info("Looting")
        self.transition_time = time.time()

    def on_exit_searching(self):
        self.searching_machine = MobSearch(self.controller, self.rotation)

    def on_exit_fighting(self):
        self.fighting_machine = CombatAction(self.controller, self.rotation)

    def on_exit_restoring(self):1
        pass

    def on_exit_looting(self):
        self.looting_machine = MobLooting(self.controller, self.rotation)





