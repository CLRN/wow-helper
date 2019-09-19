from constants.enums import ObjectType
from algos.relativity import Relativity
from components.settings import Settings
from scipy.spatial.kdtree import KDTree

import math

import logging


class MobPicker:
    def __init__(self, manager, starting_point):
        self.manager = manager
        self.starting_point = starting_point
        self.level = self.manager.player().level()

        self.alive_mobs = list()
        self.alive_mobs_tree = None

    def update(self):
        # load all mobs to a quad tree
        points = list()
        self.alive_mobs = filter(self._filter_alive, self.manager.objects())
        for mob in self.alive_mobs:
            points.append([mob.x(), mob.y()])

        self.alive_mobs_tree = KDTree(points)

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
        player = self.manager.player()
        to_starting_point = Relativity.distance(player, self.starting_point)
        if to_starting_point > Settings.FARMING_RANGE:
            return self.starting_point

        distance, location = self.alive_mobs_tree.query([player.x(), player.y()], k=5)
        for mob_id in location:
            group, _ = self.alive_mobs_tree.query([self.alive_mobs[mob_id].x(), self.alive_mobs[mob_id].y()],
                                                  distance_upper_bound=Settings.MOB_GROUP_PROXIMITY_RANGE,
                                                  k=Settings.MOB_GROUP_PROXIMITY_COUNT)
            nearby = [x for x in filter(lambda x: x != math.inf, group)]
            if len(nearby) + 1 < Settings.MOB_GROUP_PROXIMITY_COUNT:
                return self.alive_mobs[mob_id]

        return self.starting_point

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
