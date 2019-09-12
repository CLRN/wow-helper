from units.unit import Unit
from constants.offsets import Offsets

import math


class Player(Unit):
    def spell(self):
        return self.process.int(self.offset + Offsets.CurrentSpellId)

    def is_attacking(self):
        return self.process.int(self.offset + Offsets.IsAttacking) != 0

    def auras(self):
        offset = self.offset + Offsets.FirstAuraOffset

        result = list()
        for i in range(0, 20):
            aura = self.process.int(offset)
            if aura:
                result.append(aura)
            offset += Offsets.NextAuraOffset
        return result
