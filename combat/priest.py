from components.spell import Spell


class Model:
    def __init__(self, player_settings):
        self.player_settings = player_settings

    def get_next_attacking_spell(self):
        return Spell(2, 25, 2, self.player_settings.smite(), 0)

    def get_next_power_regen_spell(self):
        return Spell(0, 30, 10, self.player_settings.drink(), 10)

    def get_healing_spell(self):
        return Spell(2, 25, 2, self.player_settings.heal(), 0)
