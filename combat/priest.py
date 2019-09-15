from components.spell import Spell

FORTITUDE = 1245


class Model:
    def __init__(self, player_settings, object_manager):
        self.player_settings = player_settings
        self.object_manager = object_manager

    def get_next_attacking_spell(self, mobs):
        return Spell(0, 2, 25, 2, self.player_settings.smite(), 0)

    def get_next_power_regen_spell(self):
        return Spell(0, 0, 30, 10, self.player_settings.drink(), 10)

    def get_healing_spell(self):
        return Spell(0, 2, 25, 2, self.player_settings.heal(), 0)
