from constants.enums import ObjectType
from algos.relativity import Relativity
from components.settings import Settings

import math

import logging


class MobPicker:
    def __init__(self, manager, starting_point):
        self.manager = manager
        self.starting_point = starting_point
        self.level = self.manager.player().level()

    def _filter_alive(self, mob):
        if mob.target():
            return False
        if mob.npc_flags() or mob.type() != ObjectType.Unit or \
           mob.level() - self.level > Settings.HIGHER_LEVEL_MOB_THRESHOLD or \
           self.level - mob.level() > Settings.LOWER_LEVEL_MOB_THRESHOLD or \
           mob.faction() in Settings.FRIENDLY_FACTIONS or \
           mob.summoned():
            return False
        return mob.hp() != 0

    def _filter_lootable(self, mob):
        if mob.target():
            return False
        return not mob.npc_flags() and mob.type() == ObjectType.Unit and not mob.hp() and (mob.loot() or mob.skin())

    def _count_proximity(self, mob, range):
        count = 0
        mobs = list()
        for o in self.manager.objects():
            if o != mob and o.type() == ObjectType.Unit:
                mobs.append((Relativity.distance(mob, o), o))

        for range_to, mob in mobs:
            if range_to <= range:
                count += 1
        return count

    def _pick(self, filter_func):
        player = self.manager.player()
        self.level = player.level()

        # filter out units keeping mobs only
        mobs = filter(filter_func, self.manager.objects())
        return sorted(mobs, key=lambda x: Relativity.distance(player, x))

    def pick_alive(self):
        to_starting_point = Relativity.distance(self.manager.player(), self.starting_point)
        if to_starting_point > Settings.FARMING_RANGE:
            return self.starting_point
        elif to_starting_point > Settings.FARMING_RANGE / 2:
            ordered = self._pick(self._filter_alive)
            ordered = sorted(ordered, key=lambda x: Relativity.distance(self.starting_point, x))
        else:
            ordered = self._pick(self._filter_alive)

        while len(ordered):
            # check proximity for nearby mobs
            mob = ordered[0]
            if self._count_proximity(mob, Settings.MOB_GROUP_PROXIMITY_RANGE) + 1 >= Settings.MOB_GROUP_PROXIMITY_COUNT:
                ordered.pop(0)
            else:
                break
        return ordered[0] if len(ordered) else None

    def pick_closest(self):
        ordered = self._pick(self._filter_alive)
        return ordered[0] if len(ordered) else None

    def pick_lootable(self):
        ordered = self._pick(self._filter_lootable)
        return ordered[0] if len(ordered) else None

    def fighting(self):
        player_id = self.manager.player().id()

        # filter out units keeping mobs only
        result = list()
        for m in self.manager.objects():
            if m.hp() and m.target() == player_id and m.type() == ObjectType.Unit:
                result.append(m)

        return result
