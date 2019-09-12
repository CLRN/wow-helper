from statemachine import StateMachine, State
from algos.relativity import Relativity
from components.settings import Settings
from machines.rotation import Rotation
from machines.looting import MobLooting
from machines.mob_search import MobSearch
from machines.combat_action import CombatAction

import logging
import time


class MobFarmer(StateMachine):
    searching = State('Searching for next mob')
    fighting = State('Fighting with mob')
    looting = State('Looting mobs', initial=True)
    restoring = State('Restoring HP/Power')

    found = searching.to(fighting)
    lost = fighting.to(searching)
    killed = fighting.to(looting)
    looted = looting.to(restoring)
    restored = restoring.to(searching)
    fight = searching.to(fighting) | restoring.to(fighting) | looting.to(fighting)

    def __init__(self, controller, object_manager, combat_model, mob_picker):
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

    def _do_searching(self):
        mob = self.mob_picker.pick_alive()
        if not mob:
            logging.warning("Can't find any mobs nearby")
            return

        distance = Relativity.distance(self.object_manager.player(), mob)
        target = self.object_manager.target()

        self._rotate(mob)
        self.search.process(distance, target.id() == mob.id() if target else False)
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
                                self.combat_model.get_next_spell(),
                                player.spell())

    def _do_restoring(self):
        player = self.object_manager.player()
        if (player.hp() * 100) / player.max_hp() > Settings.REGEN_HP_THRESHOLD and \
           (player.power() * 100) / player.max_power() > Settings.REGEN_POWER_THRESHOLD:
            self.restored()
        elif (player.hp() * 100) / player.max_hp() < Settings.REGEN_HP_THRESHOLD and \
             (player.power() * 100) / player.max_power() > Settings.REGEN_POWER_THRESHOLD and \
                self.combat_model.can_heal():
            self.combat_model.heal_self()
        else:
            # TODO: do some power restoration
            pass

    def _do_looting(self):
        mob = self.mob_picker.pick_lootable()
        if not mob and time.time() - self.transition_time > Settings.TRANSITION_TIME_LOOTING:
            self.looted()
        elif mob:
            self._rotate(mob)
            self.looting.process(Relativity.distance(self.object_manager.player(), mob))

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





