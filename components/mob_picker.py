from constants.enums import ObjectType
from algos.relativity import Relativity

import math

MAX_LEVEL_DIFF = 2


class MobPicker:
    def __init__(self, manager):
        self.manager = manager
        self.level = self.manager.player().level()

    def _filter_alive(self, mob):
        if mob.target():
            return False
        if mob.npc_flags() or mob.type() != ObjectType.Unit or math.fabs(mob.level() - self.level) > MAX_LEVEL_DIFF:
            return False
        return mob.hp() != 0

    def _filter_lootable(self, mob):
        if mob.target():
            return False
        return not mob.npc_flags() and mob.type() == ObjectType.Unit and not mob.hp() and mob.loot()

    def _pick(self, filter_func):
        player = self.manager.player()
        self.level = player.level()

        # filter out units keeping mobs only
        mobs = filter(filter_func, self.manager.objects())
        ordered = sorted(mobs, key=lambda x: Relativity.distance(player, x))

        return ordered[0] if len(ordered) else None

    def pick_alive(self):
        return self._pick(self._filter_alive)

    def pick_lootable(self):
        return self._pick(self._filter_lootable)
