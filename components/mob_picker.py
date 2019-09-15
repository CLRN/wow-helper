from constants.enums import ObjectType
from algos.relativity import Relativity
from components.settings import Settings

import math

import logging


class MobPicker:
    def __init__(self, manager):
        self.manager = manager
        self.level = self.manager.player().level()

    def _filter_alive(self, mob):
        if mob.target():
            return False
        if mob.npc_flags() or mob.type() != ObjectType.Unit or \
           mob.level() - self.level > Settings.HIGHER_LEVEL_MOB_THRESHOLD or \
           self.level - mob.level() > Settings.LOWER_LEVEL_MOB_THRESHOLD or \
           mob.summoned():
            return False
        return mob.hp() != 0

    def _filter_lootable(self, mob):
        if mob.target():
            return False
        return not mob.npc_flags() and mob.type() == ObjectType.Unit and not mob.hp() and (mob.loot() or mob.skin())

    def _count_proximity(self, mob, range):
        count = 0
        for o in self.manager.objects():
            if o != mob and mob.type() == ObjectType.Unit and Relativity.distance(mob, o) < range:
                count += 1
        return count

    def _pick(self, filter_func):
        player = self.manager.player()
        self.level = player.level()

        # filter out units keeping mobs only
        mobs = filter(filter_func, self.manager.objects())
        ordered = sorted(mobs, key=lambda x: Relativity.distance(player, x))

        while len(ordered):
            # check proximity for nearby mobs
            mob = ordered[0]
            if self._count_proximity(mob, Settings.MOB_GROUP_PROXIMITY_RANGE) > 2:
                logging.info(f"Skipping mob {mob} because it has several mobs nearby withing range {Settings.MOB_GROUP_PROXIMITY_RANGE}")
                ordered.pop(0)
            else:
                break

        return ordered[0] if len(ordered) else None

    def pick_alive(self):
        return self._pick(self._filter_alive)

    def pick_lootable(self):
        return self._pick(self._filter_lootable)

    def fighting(self):
        player_id = self.manager.player().id()

        # filter out units keeping mobs only
        result = list()
        for m in self.manager.objects():
            if m.hp() and m.target() == player_id and m.type() == ObjectType.Unit:
                result.append(m)

        return result
