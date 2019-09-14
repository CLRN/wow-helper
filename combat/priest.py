from components.spell import Spell


class Model:
    def get_next_attacking_spell(self):
        return Spell(2, 25, 2, '2', 0)

    def get_next_power_regen_spell(self):
        return Spell(0, 30, 10, '7', 10)