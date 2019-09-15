from components.spell import Spell
from components.settings import Settings

CAT_FORM = 768
MARK_OF_THE_WILD = 6756
REJUVENATION = 2090
REGROWTH = 8938


class Model:
    def __init__(self, player_settings, object_manager):
        self.player_settings = player_settings
        self.object_manager = object_manager

    def _heal(self, auras):
        if CAT_FORM in auras:
            return Spell(CAT_FORM, 0, 100, 0, self.player_settings.cat_form(), 0)  # remove cat form
        elif REGROWTH not in auras:
            return Spell(REGROWTH, 0, 100, 2, self.player_settings.regrowth(), 0)
        elif REJUVENATION not in auras:
            return Spell(REJUVENATION, 0, 100, 0, self.player_settings.regrowth(), 0)

    def get_next_attacking_spell(self, mobs):
        # check auras first
        player = self.object_manager.player()
        auras = player.auras()

        # check case when we need to heal in combat
        if (player.hp() * 100) / player.max_hp() < Settings.HEAL_IN_COMBAT_THRESHOLD and REJUVENATION not in auras:
            spell = self._heal(auras)
            if spell:
                return spell

        if CAT_FORM not in auras:
            return Spell(CAT_FORM, 0, 100, 0, self.player_settings.cat_form(), 0)

        return Spell(0, 2, 25, 2, self.player_settings.attack(), 0)

    def get_next_power_regen_spell(self):
        return Spell(0, 0, 30, 10, self.player_settings.drink(), 10)

    def get_healing_spell(self):
        return self._heal(self.object_manager.player().auras())
