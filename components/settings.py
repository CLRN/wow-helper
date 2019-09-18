class Settings:
    SEARCH_ANGLE_RANGE = 20
    ATTACK_ANGLE_RANGE = 30
    FLEE_ANGLE_RANGE = 60

    REGEN_HP_THRESHOLD = 80
    REGEN_POWER_THRESHOLD = 60

    HEAL_IN_COMBAT_THRESHOLD = 30

    FLEE_HP_THRESHOLD = 40
    FLEE_POWER_THRESHOLD = 40

    LOOTING_RANGE = 4

    HIGHER_LEVEL_MOB_THRESHOLD = 2
    LOWER_LEVEL_MOB_THRESHOLD = 4

    SEARCH_RANGE = 20

    MIN_ACTION_DELAY_SECONDS = 0.3
    LOOT_ACTION_DELAY_SECONDS = 2
    LOOT_ACTION_REPEAT_SECONDS = 3

    MOB_GROUP_PROXIMITY_RANGE = 20  # range between mobs to consider them a group
    MOB_GROUP_PROXIMITY_COUNT = 3  # do not engage in combat if a group has that many mobs

    REPORTING_TIME = 10

    FARMING_RANGE = 100

    WAYPOINTS_FILE = 'waypoints.dat'
    WAYPOINTS_MIN_DISTANCE = 10

    FRIENDLY_FACTIONS = [83]  # read from db
