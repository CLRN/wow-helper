from units.object import Object
from constants.descriptors import CGUnitData, CGObjectData


class Unit(Object):
    def hp(self):
        return self.process.int(self.descriptors + CGUnitData.health * 4)

    def power(self):
        return self.process.int(self.descriptors + CGUnitData.power * 4)

    def level(self):
        return self.process.int(self.descriptors + CGUnitData.level * 4)

    def target(self):
        return self.process.int(self.descriptors + CGUnitData.target * 4)

    def npc_flags(self):
        return self.process.int(self.descriptors + CGUnitData.npcFlags * 4)

    def loot(self):
        return self.process.byte(self.descriptors + CGObjectData.m_entryID * 4) == 4
