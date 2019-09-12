from constants.enums import ObjectType
from algos.relativity import Relativity

import math

MAX_LEVEL_DIFF = 2


class MobPicker:
    def __init__(self, manager, alive=True):
        self.manager = manager
        self.level = self.manager.player().level()
        self.pick_alive = alive

    def _mob_filter(self, mob):
        if mob.target():
            return False
        if mob.npc_flags() or mob.type() != ObjectType.Unit or math.fabs(mob.level() - self.level) > MAX_LEVEL_DIFF:
            return False
        if self.pick_alive and mob.hp():
            return True

        return False

    def pick(self):
        player = self.manager.player()
        self.level = player.level()

        # filter out units keeping mobs only
        mobs = filter(self._mob_filter, self.manager.objects())
        ordered = sorted(mobs, key=lambda x: Relativity.distance(player, x))

        return ordered[0] if len(ordered) else None
