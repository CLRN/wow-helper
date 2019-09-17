from units.unit import Unit
from constants.manual_offsets import ObjectOffsets


class Player(Unit):
    def spell(self):
        return self.process.int(self.offset + ObjectOffsets.CurrentSpellId)

    def is_attacking(self):
        return self.process.int(self.offset + ObjectOffsets.IsAttacking) != 0

