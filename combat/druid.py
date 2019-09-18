from components.spell import Spell
from components.settings import Settings
from algos.relativity import Relativity
import time


MARK_OF_THE_WILD = 6756
THORNS = 1075  # rank 3
CAT_FORM = 768
REJUVENATION = 2090  # rank 4
REGROWTH = 8939  # rank 3
TIGERS_FURY = 5217  # rank 1
RAKE = 1822  # rank 1


class Model:
    def __init__(self, player_settings, object_manager):
        self.player_settings = player_settings
        self.object_manager = object_manager

        self.cat = Spell(CAT_FORM, 0, 100, 0, self.player_settings.cat_form(), 0)
        self.rejuvenation = Spell(REJUVENATION, 0, 100, 0, self.player_settings.rejuvenation(), 0)

    def _heal(self, auras):
        player = self.object_manager.player()
        if CAT_FORM in auras:
            return self.cat  # remove cat form
        elif REGROWTH not in auras and (player.hp() * 100) / player.max_hp() < 70:
            return Spell(REGROWTH, 0, 100, 2, self.player_settings.regrowth(), 0)
        elif REJUVENATION not in auras:
            return self.rejuvenation
        elif (player.hp() * 100) / player.max_hp() < 70:
            return Spell(0, 0, 100, 3, self.player_settings.healing_touch(), 0)

    def get_next_attacking_spell(self, mobs, target):
        # check auras first
        player = self.object_manager.player()
        auras = player.auras()

        # calculate threshold based on how many mobs we're fighting with
        threshold = Settings.HEAL_IN_COMBAT_THRESHOLD + len(mobs) * 10

        # check case when we need to heal in combat
        if (player.hp() * 100) / player.max_hp() < threshold and (player.power() * 100) / player.max_power() > 40:
            spell = self._heal(auras)
            if spell:
                return spell

        if CAT_FORM not in auras:
            return self.cat

        if target.hp() == target.max_hp():
            return Spell(RAKE, 2, 4, 0, self.player_settings.rake(), 10)

        if TIGERS_FURY not in auras and Relativity.distance(player, target) < 5:
            return Spell(TIGERS_FURY, 0, 100, 0, self.player_settings.tigers_fury(), 0)

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
            return self.cat  # remove cat form
        elif MARK_OF_THE_WILD not in auras:
            return Spell(MARK_OF_THE_WILD, 0, 100, 0, self.player_settings.mark(), 0)
        elif THORNS not in auras:
            return Spell(THORNS, 0, 100, 0, self.player_settings.thorns(), 0)

    def get_need_to_flee(self, mobs):
        player = self.object_manager.player()
        hp = (player.hp() * 100) / player.max_hp() < Settings.FLEE_HP_THRESHOLD
        power = (player.power() * 100) / player.max_power() < Settings.FLEE_POWER_THRESHOLD
        return len(mobs) > 2 or (len(mobs) > 1 and hp and power)

    def get_next_fleeing_spell(self):
        auras = self.object_manager.player().auras()
        if REJUVENATION not in auras:
            return self.cat if CAT_FORM in auras else self.rejuvenation

        return self.cat if CAT_FORM not in auras else None
