from units.unit import Unit
from constants.manual_offsets import ObjectOffsets


class Player(Unit):
    def spell(self):
        return self.process.int(self.offset + ObjectOffsets.CurrentSpellId)

    def is_attacking(self):
        return self.process.int(self.offset + ObjectOffsets.IsAttacking) != 0

    def auras(self):
        offset = self.offset + ObjectOffsets.FirstAuraOffset

        result = list()
        for i in range(0, 20):
            aura = self.process.int(offset)
            if aura:
                result.append(aura)
            offset += ObjectOffsets.NextAuraOffset
        return result
