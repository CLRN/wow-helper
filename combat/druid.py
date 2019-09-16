from components.spell import Spell
from components.settings import Settings
import time


MARK_OF_THE_WILD = 6756
THORNS = 782
CAT_FORM = 768
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
            return Spell(REJUVENATION, 0, 100, 0, self.player_settings.rejuvenation(), 0)
        else:
            return Spell(0, 0, 100, 3, self.player_settings.healing_touch(), 0)

    def get_next_attacking_spell(self, mobs):
        # check auras first£
        player = self.object_manager.player()
        auras = player.auras()

        # calculate threshold based on how many mobs we're fighting with
        threshold = Settings.HEAL_IN_COMBAT_THRESHOLD + len(mobs) * 10

        # check case when we need to heal in combat
        if (player.hp() * 100) / player.max_hp() < threshold:
            spell = self._heal(auras)
            if spell:
                return spell

        if CAT_FORM not in auras:
            return Spell(CAT_FORM, 0, 100, 0, self.player_settings.cat_form(), 0)

        return Spell(0, 2, 4, 0, self.player_settings.attack(), 0)

    def get_next_power_regen_spell(self):
        return Spell(0, 0, 30, 10, self.player_settings.drink(), 10)

    def get_healing_spell(self):
        return self._heal(self.object_manager.player().auras())

    def get_next_buff(self):
        auras = self.object_manager.player().auras()
        if MARK_OF_THE_WILD in auras and THORNS in auras:
            return None

        if CAT_FORM in auras:
            return Spell(CAT_FORM, 0, 100, 0, self.player_settings.cat_form(), 0)  # remove cat form
        elif MARK_OF_THE_WILD not in auras:
            return Spell(MARK_OF_THE_WILD, 0, 100, 0, self.player_settings.mark(), 0)
        elif THORNS not in auras:
            return Spell(THORNS, 0, 100, 0, self.player_settings.thorns(), 0)