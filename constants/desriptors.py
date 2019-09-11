class CGObjectData:
    m_guid = 0  # size: 0x4, flags: MIRROR_ALL
    m_entryID = 4  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT
    m_dynamicFlags = 5  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_scale = 6  # size: 0x1, flags: MIRROR_ALL
    CGObjectDataEnd = 7


class CGItemData:
    m_owner = CGObjectData.CGObjectDataEnd + 0  # size: 0x4, flags: MIRROR_ALL
    m_containedIn = CGObjectData.CGObjectDataEnd + 4  # size: 0x4, flags: MIRROR_ALL
    m_creator = CGObjectData.CGObjectDataEnd + 8  # size: 0x4, flags: MIRROR_ALL
    m_giftCreator = CGObjectData.CGObjectDataEnd + 12  # size: 0x4, flags: MIRROR_ALL
    m_stackCount = CGObjectData.CGObjectDataEnd + 16  # size: 0x1, flags: MIRROR_OWNER
    m_expiration = CGObjectData.CGObjectDataEnd + 17  # size: 0x1, flags: MIRROR_OWNER
    m_spellCharges = CGObjectData.CGObjectDataEnd + 18  # size: 0x5, flags: MIRROR_OWNER
    m_dynamicFlags = CGObjectData.CGObjectDataEnd + 23  # size: 0x1, flags: MIRROR_ALL
    m_enchantment = CGObjectData.CGObjectDataEnd + 24  # size: 0x27, flags: MIRROR_ALL
    m_propertySeed = CGObjectData.CGObjectDataEnd + 63  # size: 0x1, flags: MIRROR_ALL
    m_randomPropertiesID = CGObjectData.CGObjectDataEnd + 64  # size: 0x1, flags: MIRROR_ALL
    m_durability = CGObjectData.CGObjectDataEnd + 65  # size: 0x1, flags: MIRROR_OWNER
    m_maxDurability = CGObjectData.CGObjectDataEnd + 66  # size: 0x1, flags: MIRROR_OWNER
    m_createPlayedTime = CGObjectData.CGObjectDataEnd + 67  # size: 0x1, flags: MIRROR_ALL
    m_modifiersMask = CGObjectData.CGObjectDataEnd + 68  # size: 0x1, flags: MIRROR_OWNER
    m_context = CGObjectData.CGObjectDataEnd + 69  # size: 0x1, flags: MIRROR_ALL
    m_artifactXP = CGObjectData.CGObjectDataEnd + 70  # size: 0x2, flags: MIRROR_OWNER
    m_itemAppearanceModID = CGObjectData.CGObjectDataEnd + 72  # size: 0x1, flags: MIRROR_OWNER
    CGItemDataEnd = CGObjectData.CGObjectDataEnd + 73


class CGContainerData:
    m_slots = CGItemData.CGItemDataEnd + 0  # size: 0x90, flags: MIRROR_ALL
    m_numSlots = CGItemData.CGItemDataEnd + 144  # size: 0x1, flags: MIRROR_ALL
    CGContainerDataEnd = CGItemData.CGItemDataEnd + 145


class CGAzeriteEmpoweredItemData:
    m_selections = CGItemData.CGItemDataEnd + 0  # size: 0x4, flags: MIRROR_ALL
    CGAzeriteEmpoweredItemDataEnd = CGItemData.CGItemDataEnd + 4


class CGAzeriteItemData:
    m_xp = CGItemData.CGItemDataEnd + 0  # size: 0x2, flags: MIRROR_ALL
    m_level = CGItemData.CGItemDataEnd + 2  # size: 0x1, flags: MIRROR_ALL
    m_auraLevel = CGItemData.CGItemDataEnd + 3  # size: 0x1, flags: MIRROR_ALL
    m_knowledgeLevel = CGItemData.CGItemDataEnd + 4  # size: 0x1, flags: MIRROR_OWNER
    m_DEBUGknowledgeWeek = CGItemData.CGItemDataEnd + 5  # size: 0x1, flags: MIRROR_OWNER
    CGAzeriteItemDataEnd = CGItemData.CGItemDataEnd + 6


class CGUnitData:
    charm = CGObjectData.CGObjectDataEnd + 0  # size: 0x4, flags: MIRROR_ALL
    summon = CGObjectData.CGObjectDataEnd + 4  # size: 0x4, flags: MIRROR_ALL
    critter = CGObjectData.CGObjectDataEnd + 8  # size: 0x4, flags: MIRROR_SELF
    charmedBy = CGObjectData.CGObjectDataEnd + 12  # size: 0x4, flags: MIRROR_ALL
    summonedBy = CGObjectData.CGObjectDataEnd + 16  # size: 0x4, flags: MIRROR_ALL
    createdBy = CGObjectData.CGObjectDataEnd + 20  # size: 0x4, flags: MIRROR_ALL
    demonCreator = CGObjectData.CGObjectDataEnd + 24  # size: 0x4, flags: MIRROR_ALL
    lookAtControllerTarget = CGObjectData.CGObjectDataEnd + 28  # size: 0x4, flags: MIRROR_ALL
    target = CGObjectData.CGObjectDataEnd + 31  # size: 0x4, flags: MIRROR_ALL
    battlePetCompanionGUID = CGObjectData.CGObjectDataEnd + 36  # size: 0x4, flags: MIRROR_ALL
    battlePetDBID = CGObjectData.CGObjectDataEnd + 40  # size: 0x2, flags: MIRROR_ALL
    channelData = CGObjectData.CGObjectDataEnd + 42  # size: 0x2, flags: MIRROR_ALL | MIRROR_URGENT
    summonedByHomeRealm = CGObjectData.CGObjectDataEnd + 44  # size: 0x1, flags: MIRROR_ALL
    displayPower = CGObjectData.CGObjectDataEnd + 45  # size: 0x1, flags: MIRROR_ALL
    overrideDisplayPowerID = CGObjectData.CGObjectDataEnd + 46  # size: 0x1, flags: MIRROR_ALL
    health = CGObjectData.CGObjectDataEnd + 47  # size: 0x2, flags: MIRROR_VIEWER_DEPENDENT
    power = CGObjectData.CGObjectDataEnd + 49  # size: 0x6, flags: MIRROR_ALL | MIRROR_URGENT_SELF_ONLY
    maxHealth = CGObjectData.CGObjectDataEnd + 55  # size: 0x2, flags: MIRROR_VIEWER_DEPENDENT
    maxPower = CGObjectData.CGObjectDataEnd + 57  # size: 0x6, flags: MIRROR_ALL
    modPowerRegen = CGObjectData.CGObjectDataEnd + 63  # size: 0x6, flags: MIRROR_SELF | MIRROR_OWNER | MIRROR_UNIT_ALL
    level = CGObjectData.CGObjectDataEnd + 69  # size: 0x1, flags: MIRROR_ALL
    effectiveLevel = CGObjectData.CGObjectDataEnd + 70  # size: 0x1, flags: MIRROR_ALL
    contentTuningID = CGObjectData.CGObjectDataEnd + 71  # size: 0x1, flags: MIRROR_ALL
    scalingLevelMin = CGObjectData.CGObjectDataEnd + 72  # size: 0x1, flags: MIRROR_ALL
    scalingLevelMax = CGObjectData.CGObjectDataEnd + 73  # size: 0x1, flags: MIRROR_ALL
    scalingLevelDelta = CGObjectData.CGObjectDataEnd + 74  # size: 0x1, flags: MIRROR_ALL
    scalingFactionGroup = CGObjectData.CGObjectDataEnd + 75  # size: 0x1, flags: MIRROR_ALL
    scalingHealthItemLevelCurveID = CGObjectData.CGObjectDataEnd + 76  # size: 0x1, flags: MIRROR_ALL
    scalingDamageItemLevelCurveID = CGObjectData.CGObjectDataEnd + 77  # size: 0x1, flags: MIRROR_ALL
    factionTemplate = CGObjectData.CGObjectDataEnd + 78  # size: 0x1, flags: MIRROR_ALL
    virtualItems = CGObjectData.CGObjectDataEnd + 79  # size: 0x6, flags: MIRROR_ALL
    flags = CGObjectData.CGObjectDataEnd + 85  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    flags2 = CGObjectData.CGObjectDataEnd + 86  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    flags3 = CGObjectData.CGObjectDataEnd + 87  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    auraState = CGObjectData.CGObjectDataEnd + 88  # size: 0x1, flags: MIRROR_ALL
    attackRoundBaseTime = CGObjectData.CGObjectDataEnd + 89  # size: 0x2, flags: MIRROR_ALL
    rangedAttackRoundBaseTime = CGObjectData.CGObjectDataEnd + 91  # size: 0x1, flags: MIRROR_SELF
    boundingRadius = CGObjectData.CGObjectDataEnd + 92  # size: 0x1, flags: MIRROR_ALL
    combatReach = CGObjectData.CGObjectDataEnd + 93  # size: 0x1, flags: MIRROR_ALL
    displayID = CGObjectData.CGObjectDataEnd + 94  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    displayScale = CGObjectData.CGObjectDataEnd + 95  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    nativeDisplayID = CGObjectData.CGObjectDataEnd + 96  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    nativeXDisplayScale = CGObjectData.CGObjectDataEnd + 97  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    mountDisplayID = CGObjectData.CGObjectDataEnd + 98  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    minDamage = CGObjectData.CGObjectDataEnd + 99  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER | MIRROR_EMPATH
    maxDamage = CGObjectData.CGObjectDataEnd + 100  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER | MIRROR_EMPATH
    minOffHandDamage = CGObjectData.CGObjectDataEnd + 101  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER | MIRROR_EMPATH
    maxOffHandDamage = CGObjectData.CGObjectDataEnd + 102  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER | MIRROR_EMPATH
    petNumber = CGObjectData.CGObjectDataEnd + 103  # size: 0x1, flags: MIRROR_ALL
    petNameTimestamp = CGObjectData.CGObjectDataEnd + 104  # size: 0x1, flags: MIRROR_ALL
    petExperience = CGObjectData.CGObjectDataEnd + 105  # size: 0x1, flags: MIRROR_OWNER
    petNextLevelExperience = CGObjectData.CGObjectDataEnd + 106  # size: 0x1, flags: MIRROR_OWNER
    modCastingSpeed = CGObjectData.CGObjectDataEnd + 107  # size: 0x1, flags: MIRROR_ALL
    modSpellHaste = CGObjectData.CGObjectDataEnd + 108  # size: 0x1, flags: MIRROR_ALL
    modHaste = CGObjectData.CGObjectDataEnd + 109  # size: 0x1, flags: MIRROR_ALL
    modRangedHaste = CGObjectData.CGObjectDataEnd + 110  # size: 0x1, flags: MIRROR_ALL
    modHasteRegen = CGObjectData.CGObjectDataEnd + 111  # size: 0x1, flags: MIRROR_ALL
    modTimeRate = CGObjectData.CGObjectDataEnd + 112  # size: 0x1, flags: MIRROR_ALL
    createdBySpell = CGObjectData.CGObjectDataEnd + 113  # size: 0x1, flags: MIRROR_ALL
    npcFlags = CGObjectData.CGObjectDataEnd + 115  # size: 0x2, flags: MIRROR_ALL | MIRROR_VIEWER_DEPENDENT
    emoteState = CGObjectData.CGObjectDataEnd + 116  # size: 0x1, flags: MIRROR_ALL
    stats = CGObjectData.CGObjectDataEnd + 117  # size: 0x5, flags: MIRROR_SELF | MIRROR_OWNER
    statPosBuff = CGObjectData.CGObjectDataEnd + 122  # size: 0x5, flags: MIRROR_SELF | MIRROR_OWNER
    statNegBuff = CGObjectData.CGObjectDataEnd + 127  # size: 0x5, flags: MIRROR_SELF | MIRROR_OWNER
    resistances = CGObjectData.CGObjectDataEnd + 132  # size: 0x7, flags: MIRROR_SELF | MIRROR_OWNER | MIRROR_EMPATH
    resistanceBuffModsPositive = CGObjectData.CGObjectDataEnd + 139  # size: 0x7, flags: MIRROR_SELF | MIRROR_OWNER
    resistanceBuffModsNegative = CGObjectData.CGObjectDataEnd + 146  # size: 0x7, flags: MIRROR_SELF | MIRROR_OWNER
    baseMana = CGObjectData.CGObjectDataEnd + 153  # size: 0x1, flags: MIRROR_ALL
    baseHealth = CGObjectData.CGObjectDataEnd + 154  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    attackPower = CGObjectData.CGObjectDataEnd + 155  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    attackPowerModPos = CGObjectData.CGObjectDataEnd + 156  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    attackPowerModNeg = CGObjectData.CGObjectDataEnd + 157  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    attackPowerMultiplier = CGObjectData.CGObjectDataEnd + 158  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    rangedAttackPower = CGObjectData.CGObjectDataEnd + 159  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    rangedAttackPowerModPos = CGObjectData.CGObjectDataEnd + 160  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    rangedAttackPowerModNeg = CGObjectData.CGObjectDataEnd + 161  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    rangedAttackPowerMultiplier = CGObjectData.CGObjectDataEnd + 162  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    mainHandWeaponAttackPower = CGObjectData.CGObjectDataEnd + 163  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    offHandWeaponAttackPower = CGObjectData.CGObjectDataEnd + 164  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    rangedWeaponAttackPower = CGObjectData.CGObjectDataEnd + 165  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    setAttackSpeedAura = CGObjectData.CGObjectDataEnd + 166  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    lifesteal = CGObjectData.CGObjectDataEnd + 167  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    minRangedDamage = CGObjectData.CGObjectDataEnd + 168  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    maxRangedDamage = CGObjectData.CGObjectDataEnd + 169  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    powerCostModifier = CGObjectData.CGObjectDataEnd + 170  # size: 0x7, flags: MIRROR_SELF | MIRROR_OWNER
    powerCostMultiplier = CGObjectData.CGObjectDataEnd + 177  # size: 0x7, flags: MIRROR_SELF | MIRROR_OWNER
    maxHealthModifier = CGObjectData.CGObjectDataEnd + 184  # size: 0x1, flags: MIRROR_SELF | MIRROR_OWNER
    hoverHeight = CGObjectData.CGObjectDataEnd + 185  # size: 0x1, flags: MIRROR_ALL
    minItemLevelCutoff = CGObjectData.CGObjectDataEnd + 186  # size: 0x1, flags: MIRROR_ALL
    minItemLevel = CGObjectData.CGObjectDataEnd + 187  # size: 0x1, flags: MIRROR_ALL
    maxItemLevel = CGObjectData.CGObjectDataEnd + 188  # size: 0x1, flags: MIRROR_ALL
    wildBattlePetLevel = CGObjectData.CGObjectDataEnd + 189  # size: 0x1, flags: MIRROR_ALL
    battlePetCompanionNameTimestamp = CGObjectData.CGObjectDataEnd + 190  # size: 0x1, flags: MIRROR_ALL
    interactSpellID = CGObjectData.CGObjectDataEnd + 191  # size: 0x1, flags: MIRROR_ALL
    stateSpellVisualID = CGObjectData.CGObjectDataEnd + 192  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    stateAnimID = CGObjectData.CGObjectDataEnd + 193  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    stateAnimKitID = CGObjectData.CGObjectDataEnd + 194  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    stateWorldEffectID = CGObjectData.CGObjectDataEnd + 195  # size: 0x4, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    scaleDuration = CGObjectData.CGObjectDataEnd + 199  # size: 0x1, flags: MIRROR_ALL
    looksLikeMountID = CGObjectData.CGObjectDataEnd + 200  # size: 0x1, flags: MIRROR_ALL
    looksLikeCreatureID = CGObjectData.CGObjectDataEnd + 201  # size: 0x1, flags: MIRROR_ALL
    lookAtControllerID = CGObjectData.CGObjectDataEnd + 202  # size: 0x1, flags: MIRROR_ALL
    guildGUID = CGObjectData.CGObjectDataEnd + 203  # size: 0x4, flags: MIRROR_ALL
    CGUnitDataEnd = CGObjectData.CGObjectDataEnd + 207


class CGPlayerData:
    duelArbiter = CGUnitData.CGUnitDataEnd + 0  # size: 0x4, flags: MIRROR_ALL
    wowAccount = CGUnitData.CGUnitDataEnd + 4  # size: 0x4, flags: MIRROR_ALL
    lootTargetGUID = CGUnitData.CGUnitDataEnd + 8  # size: 0x4, flags: MIRROR_ALL
    playerFlags = CGUnitData.CGUnitDataEnd + 12  # size: 0x1, flags: MIRROR_ALL
    playerFlagsEx = CGUnitData.CGUnitDataEnd + 13  # size: 0x1, flags: MIRROR_ALL
    guildRankID = CGUnitData.CGUnitDataEnd + 14  # size: 0x1, flags: MIRROR_ALL
    guildDeleteDate = CGUnitData.CGUnitDataEnd + 15  # size: 0x1, flags: MIRROR_ALL
    guildLevel = CGUnitData.CGUnitDataEnd + 16  # size: 0x1, flags: MIRROR_ALL
    customDisplayOption = CGUnitData.CGUnitDataEnd + 17  # size: 0x1, flags: MIRROR_ALL
    duelTeam = CGUnitData.CGUnitDataEnd + 18  # size: 0x1, flags: MIRROR_ALL
    guildTimeStamp = CGUnitData.CGUnitDataEnd + 19  # size: 0x1, flags: MIRROR_ALL
    questLog = CGUnitData.CGUnitDataEnd + 20  # size: 0x140, flags: MIRROR_PARTY
    visibleItems = CGUnitData.CGUnitDataEnd + 340  # size: 0x26, flags: MIRROR_ALL
    playerTitle = CGUnitData.CGUnitDataEnd + 378  # size: 0x1, flags: MIRROR_ALL
    fakeInebriation = CGUnitData.CGUnitDataEnd + 379  # size: 0x1, flags: MIRROR_ALL
    virtualPlayerRealm = CGUnitData.CGUnitDataEnd + 380  # size: 0x1, flags: MIRROR_ALL
    currentSpecID = CGUnitData.CGUnitDataEnd + 381  # size: 0x1, flags: MIRROR_ALL
    taxiMountAnimKitID = CGUnitData.CGUnitDataEnd + 382  # size: 0x1, flags: MIRROR_ALL
    avgItemLevel = CGUnitData.CGUnitDataEnd + 383  # size: 0x4, flags: MIRROR_ALL
    currentBattlePetBreedQuality = CGUnitData.CGUnitDataEnd + 387  # size: 0x1, flags: MIRROR_ALL
    honorLevel = CGUnitData.CGUnitDataEnd + 388  # size: 0x1, flags: MIRROR_ALL
    CGPlayerDataEnd = CGUnitData.CGUnitDataEnd + 389


class CGActivePlayerData:
    invSlots = CGPlayerData.CGPlayerDataEnd + 0  # size: 0x170, flags: MIRROR_ALL
    farsightObject = CGPlayerData.CGPlayerDataEnd + 368  # size: 0x4, flags: MIRROR_ALL
    comboTarget = CGPlayerData.CGPlayerDataEnd + 372  # size: 0x4, flags: MIRROR_ALL
    summonedBattlePetGUID = CGPlayerData.CGPlayerDataEnd + 376  # size: 0x4, flags: MIRROR_ALL
    knownTitles = CGPlayerData.CGPlayerDataEnd + 380  # size: 0xc, flags: MIRROR_ALL
    coinage = CGPlayerData.CGPlayerDataEnd + 392  # size: 0x2, flags: MIRROR_ALL
    XP = CGPlayerData.CGPlayerDataEnd + 394  # size: 0x1, flags: MIRROR_ALL
    nextLevelXP = CGPlayerData.CGPlayerDataEnd + 395  # size: 0x1, flags: MIRROR_ALL
    trialXP = CGPlayerData.CGPlayerDataEnd + 396  # size: 0x1, flags: MIRROR_ALL
    skill = CGPlayerData.CGPlayerDataEnd + 397  # size: 0x380, flags: MIRROR_ALL
    characterPoints = CGPlayerData.CGPlayerDataEnd + 1293  # size: 0x1, flags: MIRROR_ALL
    maxTalentTiers = CGPlayerData.CGPlayerDataEnd + 1294  # size: 0x1, flags: MIRROR_ALL
    trackCreatureMask = CGPlayerData.CGPlayerDataEnd + 1295  # size: 0x1, flags: MIRROR_ALL
    trackResourceMask = CGPlayerData.CGPlayerDataEnd + 1296  # size: 0x2, flags: MIRROR_ALL
    mainhandExpertise = CGPlayerData.CGPlayerDataEnd + 1298  # size: 0x1, flags: MIRROR_ALL
    offhandExpertise = CGPlayerData.CGPlayerDataEnd + 1299  # size: 0x1, flags: MIRROR_ALL
    rangedExpertise = CGPlayerData.CGPlayerDataEnd + 1300  # size: 0x1, flags: MIRROR_ALL
    combatRatingExpertise = CGPlayerData.CGPlayerDataEnd + 1301  # size: 0x1, flags: MIRROR_ALL
    blockPercentage = CGPlayerData.CGPlayerDataEnd + 1302  # size: 0x1, flags: MIRROR_ALL
    dodgePercentage = CGPlayerData.CGPlayerDataEnd + 1303  # size: 0x1, flags: MIRROR_ALL
    dodgePercentageFromAttribute = CGPlayerData.CGPlayerDataEnd + 1304  # size: 0x1, flags: MIRROR_ALL
    parryPercentage = CGPlayerData.CGPlayerDataEnd + 1305  # size: 0x1, flags: MIRROR_ALL
    parryPercentageFromAttribute = CGPlayerData.CGPlayerDataEnd + 1306  # size: 0x1, flags: MIRROR_ALL
    critPercentage = CGPlayerData.CGPlayerDataEnd + 1307  # size: 0x1, flags: MIRROR_ALL
    rangedCritPercentage = CGPlayerData.CGPlayerDataEnd + 1308  # size: 0x1, flags: MIRROR_ALL
    offhandCritPercentage = CGPlayerData.CGPlayerDataEnd + 1309  # size: 0x1, flags: MIRROR_ALL
    spellCritPercentage = CGPlayerData.CGPlayerDataEnd + 1310  # size: 0x1, flags: MIRROR_ALL
    shieldBlock = CGPlayerData.CGPlayerDataEnd + 1311  # size: 0x1, flags: MIRROR_ALL
    mastery = CGPlayerData.CGPlayerDataEnd + 1312  # size: 0x1, flags: MIRROR_ALL
    speed = CGPlayerData.CGPlayerDataEnd + 1313  # size: 0x1, flags: MIRROR_ALL
    avoidance = CGPlayerData.CGPlayerDataEnd + 1314  # size: 0x1, flags: MIRROR_ALL
    sturdiness = CGPlayerData.CGPlayerDataEnd + 1315  # size: 0x1, flags: MIRROR_ALL
    versatility = CGPlayerData.CGPlayerDataEnd + 1316  # size: 0x1, flags: MIRROR_ALL
    versatilityBonus = CGPlayerData.CGPlayerDataEnd + 1317  # size: 0x1, flags: MIRROR_ALL
    pvpPowerDamage = CGPlayerData.CGPlayerDataEnd + 1318  # size: 0x1, flags: MIRROR_ALL
    pvpPowerHealing = CGPlayerData.CGPlayerDataEnd + 1319  # size: 0x1, flags: MIRROR_ALL
    exploredZones = CGPlayerData.CGPlayerDataEnd + 1320  # size: 0x140, flags: MIRROR_ALL
    restInfo = CGPlayerData.CGPlayerDataEnd + 1640  # size: 0x4, flags: MIRROR_ALL
    modDamageDonePos = CGPlayerData.CGPlayerDataEnd + 1644  # size: 0x7, flags: MIRROR_ALL
    modDamageDoneNeg = CGPlayerData.CGPlayerDataEnd + 1651  # size: 0x7, flags: MIRROR_ALL
    modDamageDonePercent = CGPlayerData.CGPlayerDataEnd + 1658  # size: 0x7, flags: MIRROR_ALL
    modHealingDonePos = CGPlayerData.CGPlayerDataEnd + 1665  # size: 0x1, flags: MIRROR_ALL
    modHealingPercent = CGPlayerData.CGPlayerDataEnd + 1666  # size: 0x1, flags: MIRROR_ALL
    modHealingDonePercent = CGPlayerData.CGPlayerDataEnd + 1667  # size: 0x1, flags: MIRROR_ALL
    modPeriodicHealingDonePercent = CGPlayerData.CGPlayerDataEnd + 1668  # size: 0x1, flags: MIRROR_ALL
    weaponDmgMultipliers = CGPlayerData.CGPlayerDataEnd + 1669  # size: 0x3, flags: MIRROR_ALL
    weaponAtkSpeedMultipliers = CGPlayerData.CGPlayerDataEnd + 1672  # size: 0x3, flags: MIRROR_ALL
    modSpellPowerPercent = CGPlayerData.CGPlayerDataEnd + 1675  # size: 0x1, flags: MIRROR_ALL
    modResiliencePercent = CGPlayerData.CGPlayerDataEnd + 1676  # size: 0x1, flags: MIRROR_ALL
    overrideSpellPowerByAPPercent = CGPlayerData.CGPlayerDataEnd + 1677  # size: 0x1, flags: MIRROR_ALL
    overrideAPBySpellPowerPercent = CGPlayerData.CGPlayerDataEnd + 1678  # size: 0x1, flags: MIRROR_ALL
    modTargetResistance = CGPlayerData.CGPlayerDataEnd + 1679  # size: 0x1, flags: MIRROR_ALL
    modTargetPhysicalResistance = CGPlayerData.CGPlayerDataEnd + 1680  # size: 0x1, flags: MIRROR_ALL
    localFlags = CGPlayerData.CGPlayerDataEnd + 1681  # size: 0x1, flags: MIRROR_ALL
    ammoID = CGPlayerData.CGPlayerDataEnd + 1682  # size: 0x1, flags: MIRROR_ALL
    pvpMedals = CGPlayerData.CGPlayerDataEnd + 1683  # size: 0x1, flags: MIRROR_ALL
    buybackPrice = CGPlayerData.CGPlayerDataEnd + 1684  # size: 0xc, flags: MIRROR_ALL
    buybackTimestamp = CGPlayerData.CGPlayerDataEnd + 1696  # size: 0xc, flags: MIRROR_ALL
    thisWeekContribution = CGPlayerData.CGPlayerDataEnd + 1708  # size: 0x1, flags: MIRROR_ALL
    lifetimeHonorableKills = CGPlayerData.CGPlayerDataEnd + 1709  # size: 0x1, flags: MIRROR_ALL
    lifetimeDishonorableKills = CGPlayerData.CGPlayerDataEnd + 1710  # size: 0x1, flags: MIRROR_ALL
    yesterdayContribution = CGPlayerData.CGPlayerDataEnd + 1711  # size: 0x1, flags: MIRROR_ALL
    lastWeekContribution = CGPlayerData.CGPlayerDataEnd + 1712  # size: 0x1, flags: MIRROR_ALL
    lastWeekRank = CGPlayerData.CGPlayerDataEnd + 1713  # size: 0x1, flags: MIRROR_ALL
    watchedFactionIndex = CGPlayerData.CGPlayerDataEnd + 1714  # size: 0x1, flags: MIRROR_ALL
    combatRatings = CGPlayerData.CGPlayerDataEnd + 1715  # size: 0x20, flags: MIRROR_ALL
    pvpInfo = CGPlayerData.CGPlayerDataEnd + 1747  # size: 0x36, flags: MIRROR_ALL
    maxLevel = CGPlayerData.CGPlayerDataEnd + 1801  # size: 0x1, flags: MIRROR_ALL
    scalingPlayerLevelDelta = CGPlayerData.CGPlayerDataEnd + 1802  # size: 0x1, flags: MIRROR_ALL
    maxCreatureScalingLevel = CGPlayerData.CGPlayerDataEnd + 1803  # size: 0x1, flags: MIRROR_ALL
    noReagentCostMask = CGPlayerData.CGPlayerDataEnd + 1804  # size: 0x4, flags: MIRROR_ALL
    petSpellPower = CGPlayerData.CGPlayerDataEnd + 1808  # size: 0x1, flags: MIRROR_ALL
    professionSkillLine = CGPlayerData.CGPlayerDataEnd + 1809  # size: 0x2, flags: MIRROR_ALL
    uiHitModifier = CGPlayerData.CGPlayerDataEnd + 1811  # size: 0x1, flags: MIRROR_ALL
    uiSpellHitModifier = CGPlayerData.CGPlayerDataEnd + 1812  # size: 0x1, flags: MIRROR_ALL
    homeRealmTimeOffset = CGPlayerData.CGPlayerDataEnd + 1813  # size: 0x1, flags: MIRROR_ALL
    modPetHaste = CGPlayerData.CGPlayerDataEnd + 1814  # size: 0x1, flags: MIRROR_ALL
    overrideSpellsID = CGPlayerData.CGPlayerDataEnd + 1815  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT_SELF_ONLY
    lfgBonusFactionID = CGPlayerData.CGPlayerDataEnd + 1816  # size: 0x1, flags: MIRROR_ALL
    lootSpecID = CGPlayerData.CGPlayerDataEnd + 1817  # size: 0x1, flags: MIRROR_ALL
    overrideZonePVPType = CGPlayerData.CGPlayerDataEnd + 1818  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT_SELF_ONLY
    bagSlotFlags = CGPlayerData.CGPlayerDataEnd + 1819  # size: 0x4, flags: MIRROR_ALL
    bankBagSlotFlags = CGPlayerData.CGPlayerDataEnd + 1823  # size: 0x6, flags: MIRROR_ALL
    questCompleted = CGPlayerData.CGPlayerDataEnd + 1829  # size: 0x6d6, flags: MIRROR_ALL
    honor = CGPlayerData.CGPlayerDataEnd + 3579  # size: 0x1, flags: MIRROR_ALL
    honorNextLevel = CGPlayerData.CGPlayerDataEnd + 3580  # size: 0x1, flags: MIRROR_ALL
    pvpTierMaxFromWins = CGPlayerData.CGPlayerDataEnd + 3581  # size: 0x1, flags: MIRROR_ALL
    pvpLastWeeksTierMaxFromWins = CGPlayerData.CGPlayerDataEnd + 3582  # size: 0x1, flags: MIRROR_ALL
    CGActivePlayerDataEnd = CGPlayerData.CGPlayerDataEnd + 3583


class CGGameObjectData:
    m_createdBy = CGObjectData.CGObjectDataEnd + 0  # size: 0x4, flags: MIRROR_ALL
    m_guildGUID = CGObjectData.CGObjectDataEnd + 4  # size: 0x4, flags: MIRROR_ALL
    m_displayID = CGObjectData.CGObjectDataEnd + 8  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_flags = CGObjectData.CGObjectDataEnd + 9  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    m_parentRotation = CGObjectData.CGObjectDataEnd + 10  # size: 0x4, flags: MIRROR_ALL
    m_factionTemplate = CGObjectData.CGObjectDataEnd + 14  # size: 0x1, flags: MIRROR_ALL
    m_level = CGObjectData.CGObjectDataEnd + 15  # size: 0x1, flags: MIRROR_ALL
    m_spellVisualID = CGObjectData.CGObjectDataEnd + 16  # size: 0x1, flags: MIRROR_ALL | MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_stateSpellVisualID = CGObjectData.CGObjectDataEnd + 17  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_spawnTrackingStateAnimID = CGObjectData.CGObjectDataEnd + 18  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_spawnTrackingStateAnimKitID = CGObjectData.CGObjectDataEnd + 19  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_stateWorldEffectID = CGObjectData.CGObjectDataEnd + 20  # size: 0x4, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_customParam = CGObjectData.CGObjectDataEnd + 24  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    CGGameObjectDataEnd = CGObjectData.CGObjectDataEnd + 25


class CGDynamicObjectData:
    m_caster = CGObjectData.CGObjectDataEnd + 0  # size: 0x4, flags: MIRROR_ALL
    m_type = CGObjectData.CGObjectDataEnd + 4  # size: 0x1, flags: MIRROR_ALL
    m_spellXSpellVisualID = CGObjectData.CGObjectDataEnd + 5  # size: 0x1, flags: MIRROR_ALL
    m_spellID = CGObjectData.CGObjectDataEnd + 6  # size: 0x1, flags: MIRROR_ALL
    m_radius = CGObjectData.CGObjectDataEnd + 7  # size: 0x1, flags: MIRROR_ALL
    m_castTime = CGObjectData.CGObjectDataEnd + 8  # size: 0x1, flags: MIRROR_ALL
    CGDynamicObjectDataEnd = CGObjectData.CGObjectDataEnd + 9


class CGCorpseData:
    m_owner = CGObjectData.CGObjectDataEnd + 0  # size: 0x4, flags: MIRROR_ALL
    m_partyGUID = CGObjectData.CGObjectDataEnd + 4  # size: 0x4, flags: MIRROR_ALL
    m_guildGUID = CGObjectData.CGObjectDataEnd + 8  # size: 0x4, flags: MIRROR_ALL
    m_displayID = CGObjectData.CGObjectDataEnd + 12  # size: 0x1, flags: MIRROR_ALL
    m_items = CGObjectData.CGObjectDataEnd + 13  # size: 0x13, flags: MIRROR_ALL
    m_flags = CGObjectData.CGObjectDataEnd + 32  # size: 0x1, flags: MIRROR_ALL
    m_dynamicFlags = CGObjectData.CGObjectDataEnd + 33  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT
    m_factionTemplate = CGObjectData.CGObjectDataEnd + 34  # size: 0x1, flags: MIRROR_ALL
    m_customDisplayOption = CGObjectData.CGObjectDataEnd + 35  # size: 0x1, flags: MIRROR_ALL
    CGCorpseDataEnd = CGObjectData.CGObjectDataEnd + 36


class CGAreaTriggerData:
    m_overrideScaleCurve = CGObjectData.CGObjectDataEnd + 0  # size: 0x7, flags: MIRROR_ALL | MIRROR_URGENT
    m_extraScaleCurve = CGObjectData.CGObjectDataEnd + 7  # size: 0x7, flags: MIRROR_ALL | MIRROR_URGENT
    m_caster = CGObjectData.CGObjectDataEnd + 14  # size: 0x4, flags: MIRROR_ALL
    m_duration = CGObjectData.CGObjectDataEnd + 18  # size: 0x1, flags: MIRROR_ALL
    m_timeToTarget = CGObjectData.CGObjectDataEnd + 19  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    m_timeToTargetScale = CGObjectData.CGObjectDataEnd + 20  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    m_timeToTargetExtraScale = CGObjectData.CGObjectDataEnd + 21  # size: 0x1, flags: MIRROR_ALL | MIRROR_URGENT
    m_spellID = CGObjectData.CGObjectDataEnd + 22  # size: 0x1, flags: MIRROR_ALL
    m_spellForVisuals = CGObjectData.CGObjectDataEnd + 23  # size: 0x1, flags: MIRROR_ALL
    m_spellXSpellVisualID = CGObjectData.CGObjectDataEnd + 24  # size: 0x1, flags: MIRROR_ALL
    m_boundsRadius2D = CGObjectData.CGObjectDataEnd + 25  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT | MIRROR_URGENT
    m_decalPropertiesID = CGObjectData.CGObjectDataEnd + 26  # size: 0x1, flags: MIRROR_ALL
    m_creatingEffectGUID = CGObjectData.CGObjectDataEnd + 27  # size: 0x4, flags: MIRROR_ALL
    CGAreaTriggerDataEnd = CGObjectData.CGObjectDataEnd + 31


class CGSceneObjectData:
    m_scriptPackageID = CGObjectData.CGObjectDataEnd + 0  # size: 0x1, flags: MIRROR_ALL
    m_rndSeedVal = CGObjectData.CGObjectDataEnd + 1  # size: 0x1, flags: MIRROR_ALL
    m_createdBy = CGObjectData.CGObjectDataEnd + 2  # size: 0x4, flags: MIRROR_ALL
    m_sceneType = CGObjectData.CGObjectDataEnd + 6  # size: 0x1, flags: MIRROR_ALL
    CGSceneObjectDataEnd = CGObjectData.CGObjectDataEnd + 7


class CGConversationData:
    m_lastLineEndTime = CGObjectData.CGObjectDataEnd + 0  # size: 0x1, flags: MIRROR_VIEWER_DEPENDENT
    CGConversationDataEnd = CGObjectData.CGObjectDataEnd + 1


class CGItemDynamicData:
    m_modifiers = CGObjectData.CGObjectDataEnd + 0  # size: 0x4, flags: MIRROR_NONE
    m_bonusListIDs = CGObjectData.CGObjectDataEnd + 4  # size: 0x104, flags: MIRROR_NONE
    m_artifactPowers = CGObjectData.CGObjectDataEnd + 264  # size: 0x4, flags: MIRROR_NONE
    m_gems = CGObjectData.CGObjectDataEnd + 268  # size: 0x4, flags: MIRROR_NONE
    CGItemDynamicDataEnd = CGObjectData.CGObjectDataEnd + 272


class CGUnitDynamicData:
    passiveSpells = CGObjectData.CGObjectDataEnd + 0  # size: 0x201, flags: MIRROR_NONE
    worldEffects = CGObjectData.CGObjectDataEnd + 513  # size: 0x201, flags: MIRROR_NONE
    channelObjects = CGObjectData.CGObjectDataEnd + 1026  # size: 0x201, flags: MIRROR_NONE
    CGUnitDynamicDataEnd = CGObjectData.CGObjectDataEnd + 1539


class CGPlayerDynamicData:
    arenaCooldowns = CGObjectData.CGObjectDataEnd + 0  # size: 0x1, flags: MIRROR_NONE
    CGPlayerDynamicDataEnd = CGObjectData.CGObjectDataEnd + 1


class CGActivePlayerDynamicData:
    researchSites = CGObjectData.CGObjectDataEnd + 0  # size: 0x1, flags: MIRROR_NONE
    researchSiteProgress = CGObjectData.CGObjectDataEnd + 1  # size: 0x1, flags: MIRROR_NONE
    dailyQuestsCompleted = CGObjectData.CGObjectDataEnd + 2  # size: 0x1, flags: MIRROR_NONE
    availableQuestLineXQuestIDs = CGObjectData.CGObjectDataEnd + 3  # size: 0x1, flags: MIRROR_NONE
    heirlooms = CGObjectData.CGObjectDataEnd + 4  # size: 0x1, flags: MIRROR_NONE
    heirloomFlags = CGObjectData.CGObjectDataEnd + 5  # size: 0x1, flags: MIRROR_NONE
    toys = CGObjectData.CGObjectDataEnd + 6  # size: 0x1, flags: MIRROR_NONE
    transmog = CGObjectData.CGObjectDataEnd + 7  # size: 0x1, flags: MIRROR_NONE
    conditionalTransmog = CGObjectData.CGObjectDataEnd + 8  # size: 0x1, flags: MIRROR_NONE
    selfResSpells = CGObjectData.CGObjectDataEnd + 9  # size: 0x1, flags: MIRROR_NONE
    characterRestrictions = CGObjectData.CGObjectDataEnd + 10  # size: 0x1, flags: MIRROR_NONE
    spellPctModByLabel = CGObjectData.CGObjectDataEnd + 11  # size: 0x1, flags: MIRROR_NONE
    spellFlatModByLabel = CGObjectData.CGObjectDataEnd + 12  # size: 0x1, flags: MIRROR_NONE
    research = CGObjectData.CGObjectDataEnd + 13  # size: 0x1, flags: MIRROR_NONE
    CGActivePlayerDynamicDataEnd = CGObjectData.CGObjectDataEnd + 14


class CGGameObjectDynamicData:
    enableDoodadSets = CGObjectData.CGObjectDataEnd + 0  # size: 0x1, flags: MIRROR_NONE
    CGGameObjectDynamicDataEnd = CGObjectData.CGObjectDataEnd + 1


class CGConversationDynamicData:
    m_actors = CGObjectData.CGObjectDataEnd + 0  # size: 0x1, flags: MIRROR_NONE
    m_lines = CGObjectData.CGObjectDataEnd + 1  # size: 0x100, flags: MIRROR_NONE
    CGConversationDynamicDataEnd = CGObjectData.CGObjectDataEnd + 257
