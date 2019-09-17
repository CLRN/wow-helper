from units.object import Object
from constants.descriptors import CGUnitData, CGObjectData
from constants.manual_offsets import ObjectOffsets


class Unit(Object):
    def hp(self):
        return self.process.int(self.descriptors + CGUnitData.Health * 4)

    def power(self):
        return self.process.int(self.descriptors + CGUnitData.Power * 4)

    def max_hp(self):
        return self.process.int(self.descriptors + CGUnitData.MaxHealth * 4)

    def max_power(self):
        return self.process.int(self.descriptors + CGUnitData.MaxPower * 4)

    def level(self):
        return self.process.int(self.descriptors + CGUnitData.Level * 4)

    def target(self):
        return self.process.ptr(self.descriptors + CGUnitData.Target * 4)

    def npc_flags(self):
        return self.process.int(self.descriptors + CGUnitData.NpcFlags * 4)

    def loot(self):
        return self.process.byte(self.descriptors + CGObjectData.DynamicFlags * 4) == 4

    def skin(self):
        return self.process.int(self.descriptors + CGUnitData.Flags * 4) & 0x4000000 != 0

    def summoned(self):
        return self.process.ptr(self.descriptors + CGUnitData.SummonedBy * 4)

    def auras(self):
        offset = self.offset + ObjectOffsets.FirstAuraOffset

        result = list()
        for i in range(0, 20):
            aura = self.process.int(offset)
            if aura:
                result.append(aura)
            offset += ObjectOffsets.NextAuraOffset
        return result

    def faction(self):
        return self.process.int(self.descriptors + CGUnitData.FactionTemplate * 4)
