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


class MobFarmer(StateMachine):
    searching = State('Searching for next mob')
    fighting = State('Fighting with mob')
    looting = State('Looting mobs', initial=True)
    restoring = State('Restoring HP/Power')
    eating = State('Eating/drinking to restore HP/Power')

    found = searching.to(fighting)
    lost = fighting.to(searching)
    killed = fighting.to(looting)
    looted = looting.to(restoring)
    eat = restoring.to(eating)
    restored = eating.to(searching) | restoring.to(searching)
    fight = searching.to(fighting) | restoring.to(fighting) | looting.to(fighting)

    def __init__(self, window, controller, object_manager, combat_model, mob_picker):
        self.window = window
        self.controller = controller
        self.object_manager = object_manager
        self.combat_model = combat_model

        self.mob_picker = mob_picker
        self.rotation = Rotation(self.controller)
        self.looting = MobLooting(self.controller)
        self.search = MobSearch(self.controller)
        self.combat = CombatAction(self.controller)

        self.fighting_mobs = None
        self.transition_time = time.time()

        StateMachine.__init__(self)

    def _rotate(self, unit):
        angle = Relativity.angle(self.object_manager.player(), unit)
        self.rotation.process(angle)

    def _get_coords(self, unit):
        return world_to_screen(self.object_manager.process, self.window, unit.x(), unit.y(), unit.z())

    def _do_searching(self):
        mob = self.mob_picker.pick_alive()
        if not mob:
            logging.warning("Can't find any mobs nearby")
            return

        distance = Relativity.distance(self.object_manager.player(), mob)
        target = self.object_manager.target()

        self._rotate(mob)
        self.search.process(distance, target.id() == mob.id() if target else False, self._get_coords(mob))
        if self.search.is_selected:
            self.found()

    def _do_fighting(self):
        target = self.object_manager.target()
        if not target:
            if not len(self.fighting_mobs):
                self.killed()
            else:
                self.lost()
        else:
            self._rotate(target)

            player = self.object_manager.player()
            self.combat.process(Relativity.distance(player, target),
                                self.combat_model.get_next_attacking_spell(),
                                player.spell())

    def _do_restoring(self):
        player = self.object_manager.player()
        if (player.hp() * 100) / player.max_hp() > Settings.REGEN_HP_THRESHOLD and \
           (player.power() * 100) / player.max_power() > Settings.REGEN_POWER_THRESHOLD:
            self.restored()
        elif (player.hp() * 100) / player.max_hp() < Settings.REGEN_HP_THRESHOLD and \
             (player.power() * 100) / player.max_power() > Settings.REGEN_POWER_THRESHOLD:
            spell = self.combat_model.get_healing_spell()
            if spell:
                self.controller.press(spell.bind_key)
        else:
            spell = self.combat_model.get_next_power_regen_spell()
            if spell:
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

        mob = self.mob_picker.pick_lootable()
        if not mob:
            self.looted()
        elif mob:
            self._rotate(mob)
            self.looting.process(Relativity.distance(self.object_manager.player(), mob), self._get_coords(mob))

    def process(self):
        self.fighting_mobs = self.mob_picker.fighting()
        if len(self.fighting_mobs) and not self.is_fighting:
            self.fight()
        else:
            getattr(self, f"_do_{self.current_state_value}")()

    def on_enter_searching(self):
        logging.info("Searching")
        self.transition_time = time.time()

    def on_enter_fighting(self):
        logging.info("Fighting")
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
        self.search = MobSearch(self.controller)

    def on_exit_fighting(self):
        self.combat = CombatAction(self.controller)

    def on_exit_restoring(self):
        pass

    def on_exit_looting(self):
        self.looting = MobLooting(self.controller)





