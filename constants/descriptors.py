DescriptorMulti = 0x4
DescriptorOffset = 0x10

class CGObjectData:
    Guid = 0  # size 4
    EntryID = 4  # size 1
    DynamicFlags = 5  # size 1
    Scale = 6  # size 1
    End = 7


class CGItemData:
    Owner = CGObjectData.End + 0  # size 4 flags: MIRROR_ALL
    ContainedIn = CGObjectData.End + 4  # size 4 flags: MIRROR_ALL
    Creator = CGObjectData.End + 8  # size 4 flags: MIRROR_ALL
    GiftCreator = CGObjectData.End + 12  # size 4 flags: MIRROR_ALL
    StackCount = CGObjectData.End + 16  # size 1 flags: MIRROR_OWNER
    Expiration = CGObjectData.End + 17  # size 1 flags: MIRROR_OWNER
    SpellCharges = CGObjectData.End + 18  # size 5 flags: MIRROR_OWNER
    DynamicFlags = CGObjectData.End + 23  # size 1 flags: MIRROR_ALL
    Enchantment = CGObjectData.End + 24  # size 39 flags: MIRROR_ALL
    PropertySeed = CGObjectData.End + 63  # size 1 flags: MIRROR_ALL
    RandomPropertiesID = CGObjectData.End + 64  # size 1 flags: MIRROR_ALL
    Durability = CGObjectData.End + 65  # size 1 flags: MIRROR_OWNER
    MaxDurability = CGObjectData.End + 66  # size 1 flags: MIRROR_OWNER
    CreatePlayedTime = CGObjectData.End + 67  # size 1 flags: MIRROR_ALL
    ModifiersMask = CGObjectData.End + 68  # size 1 flags: MIRROR_OWNER
    Context = CGObjectData.End + 69  # size 1 flags: MIRROR_ALL
    ArtifactXP = CGObjectData.End + 70  # size 2 flags: MIRROR_OWNER
    ItemAppearanceModID = CGObjectData.End + 72  # size 1 flags: MIRROR_OWNER
    End = CGObjectData.End + 73


class CGContainerData:
    Slots = CGItemData.End + 0  # size 144 flags: MIRROR_ALL
    NumSlots = CGItemData.End + 144  # size 1 flags: MIRROR_ALL
    End = CGItemData.End + 145


class CGAzeriteEmpoweredItemData:
    Selections = 0  # size 4
    End = 4


class CGAzeriteItemData:
    Xp = CGItemData.End + 0  # size 2 flags: MIRROR_ALL
    Level = CGItemData.End + 2  # size 1 flags: MIRROR_ALL
    AuraLevel = CGItemData.End + 3  # size 1 flags: MIRROR_ALL
    KnowledgeLevel = CGItemData.End + 4  # size 1 flags: MIRROR_OWNER
    DEBUGknowledgeWeek = CGItemData.End + 5  # size 1 flags: MIRROR_OWNER
    End = CGItemData.End + 6


class CGUnitData:
    Charm = CGObjectData.End + 0  # size 4 flags: MIRROR_ALL
    Summon = CGObjectData.End + 4  # size 4 flags: MIRROR_ALL
    Critter = CGObjectData.End + 8  # size 4 flags: MIRROR_SELF
    CharmedBy = CGObjectData.End + 12  # size 4 flags: MIRROR_ALL
    SummonedBy = CGObjectData.End + 16  # size 4 flags: MIRROR_ALL
    CreatedBy = CGObjectData.End + 20  # size 4 flags: MIRROR_ALL
    DemonCreator = CGObjectData.End + 24  # size 4 flags: MIRROR_ALL
    LookAtControllerTarget = CGObjectData.End + 28  # size 4 flags: MIRROR_ALL
    Target = CGObjectData.End + 32  # size 4 flags: MIRROR_ALL
    BattlePetCompanionGUID = CGObjectData.End + 36  # size 4 flags: MIRROR_ALL
    BattlePetDBID = CGObjectData.End + 40  # size 2 flags: MIRROR_ALL
    ChannelData = CGObjectData.End + 42  # size 2 flags: 
    SummonedByHomeRealm = CGObjectData.End + 44  # size 1 flags: MIRROR_ALL
    Sex = CGObjectData.End + 45  # size 1 flags: MIRROR_ALL
    DisplayPower = CGObjectData.End + 46  # size 1 flags: MIRROR_ALL
    OverrideDisplayPowerID = CGObjectData.End + 47  # size 1 flags: MIRROR_ALL
    Health = CGObjectData.End + 48  # size 2 flags: MIRROR_VIEWER_DEPENDENT
    Power = CGObjectData.End + 50  # size 6 flags: 
    MaxHealth = CGObjectData.End + 56  # size 2 flags: MIRROR_VIEWER_DEPENDENT
    MaxPower = CGObjectData.End + 58  # size 6 flags: MIRROR_ALL
    ModPowerRegen = CGObjectData.End + 64  # size 6 flags: 
    Level = CGObjectData.End + 70  # size 1 flags: MIRROR_ALL
    EffectiveLevel = CGObjectData.End + 71  # size 1 flags: MIRROR_ALL
    ContentTuningID = CGObjectData.End + 72  # size 1 flags: MIRROR_ALL
    ScalingLevelMin = CGObjectData.End + 73  # size 1 flags: MIRROR_ALL
    ScalingLevelMax = CGObjectData.End + 74  # size 1 flags: MIRROR_ALL
    ScalingLevelDelta = CGObjectData.End + 75  # size 1 flags: MIRROR_ALL
    ScalingFactionGroup = CGObjectData.End + 76  # size 1 flags: MIRROR_ALL
    ScalingHealthItemLevelCurveID = CGObjectData.End + 77  # size 1 flags: MIRROR_ALL
    ScalingDamageItemLevelCurveID = CGObjectData.End + 78  # size 1 flags: MIRROR_ALL
    FactionTemplate = CGObjectData.End + 79  # size 1 flags: MIRROR_ALL
    VirtualItems = CGObjectData.End + 80  # size 6 flags: MIRROR_ALL
    Flags = CGObjectData.End + 86  # size 1 flags: 
    Flags2 = CGObjectData.End + 87  # size 1 flags: 
    Flags3 = CGObjectData.End + 88  # size 1 flags: 
    AuraState = CGObjectData.End + 89  # size 1 flags: MIRROR_ALL
    AttackRoundBaseTime = CGObjectData.End + 90  # size 2 flags: MIRROR_ALL
    RangedAttackRoundBaseTime = CGObjectData.End + 92  # size 1 flags: MIRROR_SELF
    BoundingRadius = CGObjectData.End + 93  # size 1 flags: MIRROR_ALL
    CombatReach = CGObjectData.End + 94  # size 1 flags: MIRROR_ALL
    DisplayID = CGObjectData.End + 95  # size 1 flags: 
    DisplayScale = CGObjectData.End + 96  # size 1 flags: 
    NativeDisplayID = CGObjectData.End + 97  # size 1 flags: 
    NativeXDisplayScale = CGObjectData.End + 98  # size 1 flags: 
    MountDisplayID = CGObjectData.End + 99  # size 1 flags: 
    MinDamage = CGObjectData.End + 100  # size 1 flags: 
    MaxDamage = CGObjectData.End + 101  # size 1 flags: 
    MinOffHandDamage = CGObjectData.End + 102  # size 1 flags: 
    MaxOffHandDamage = CGObjectData.End + 103  # size 1 flags: 
    AnimTier = CGObjectData.End + 104  # size 1 flags: MIRROR_ALL
    PetNumber = CGObjectData.End + 105  # size 1 flags: MIRROR_ALL
    PetNameTimestamp = CGObjectData.End + 106  # size 1 flags: MIRROR_ALL
    PetExperience = CGObjectData.End + 107  # size 1 flags: MIRROR_OWNER
    PetNextLevelExperience = CGObjectData.End + 108  # size 1 flags: MIRROR_OWNER
    ModCastingSpeed = CGObjectData.End + 109  # size 1 flags: MIRROR_ALL
    ModSpellHaste = CGObjectData.End + 110  # size 1 flags: MIRROR_ALL
    ModHaste = CGObjectData.End + 111  # size 1 flags: MIRROR_ALL
    ModRangedHaste = CGObjectData.End + 112  # size 1 flags: MIRROR_ALL
    ModHasteRegen = CGObjectData.End + 113  # size 1 flags: MIRROR_ALL
    ModTimeRate = CGObjectData.End + 114  # size 1 flags: MIRROR_ALL
    CreatedBySpell = CGObjectData.End + 115  # size 1 flags: MIRROR_ALL
    NpcFlags = CGObjectData.End + 116  # size 2 flags: 
    EmoteState = CGObjectData.End + 118  # size 1 flags: MIRROR_ALL
    TrainingPointsTotal = CGObjectData.End + 119  # size 1 flags: MIRROR_OWNER
    Stats = CGObjectData.End + 120  # size 5 flags: 
    StatPosBuff = CGObjectData.End + 125  # size 5 flags: 
    StatNegBuff = CGObjectData.End + 130  # size 5 flags: 
    Resistances = CGObjectData.End + 135  # size 7 flags: 
    ResistanceBuffModsPositive = CGObjectData.End + 142  # size 7 flags: 
    ResistanceBuffModsNegative = CGObjectData.End + 149  # size 7 flags: 
    BaseMana = CGObjectData.End + 156  # size 1 flags: MIRROR_ALL
    BaseHealth = CGObjectData.End + 157  # size 1 flags: 
    ShapeshiftForm = CGObjectData.End + 158  # size 1 flags: MIRROR_ALL
    AttackPower = CGObjectData.End + 159  # size 1 flags: 
    AttackPowerModPos = CGObjectData.End + 160  # size 1 flags: 
    AttackPowerModNeg = CGObjectData.End + 161  # size 1 flags: 
    AttackPowerMultiplier = CGObjectData.End + 162  # size 1 flags: 
    RangedAttackPower = CGObjectData.End + 163  # size 1 flags: 
    RangedAttackPowerModPos = CGObjectData.End + 164  # size 1 flags: 
    RangedAttackPowerModNeg = CGObjectData.End + 165  # size 1 flags: 
    RangedAttackPowerMultiplier = CGObjectData.End + 166  # size 1 flags: 
    MainHandWeaponAttackPower = CGObjectData.End + 167  # size 1 flags: 
    OffHandWeaponAttackPower = CGObjectData.End + 168  # size 1 flags: 
    RangedWeaponAttackPower = CGObjectData.End + 169  # size 1 flags: 
    SetAttackSpeedAura = CGObjectData.End + 170  # size 1 flags: 
    Lifesteal = CGObjectData.End + 171  # size 1 flags: 
    MinRangedDamage = CGObjectData.End + 172  # size 1 flags: 
    MaxRangedDamage = CGObjectData.End + 173  # size 1 flags: 
    PowerCostModifier = CGObjectData.End + 174  # size 7 flags: 
    PowerCostMultiplier = CGObjectData.End + 181  # size 7 flags: 
    MaxHealthModifier = CGObjectData.End + 188  # size 1 flags: 
    HoverHeight = CGObjectData.End + 189  # size 1 flags: MIRROR_ALL
    MinItemLevelCutoff = CGObjectData.End + 190  # size 1 flags: MIRROR_ALL
    MinItemLevel = CGObjectData.End + 191  # size 1 flags: MIRROR_ALL
    MaxItemLevel = CGObjectData.End + 192  # size 1 flags: MIRROR_ALL
    WildBattlePetLevel = CGObjectData.End + 193  # size 1 flags: MIRROR_ALL
    BattlePetCompanionNameTimestamp = CGObjectData.End + 194  # size 1 flags: MIRROR_ALL
    InteractSpellID = CGObjectData.End + 195  # size 1 flags: MIRROR_ALL
    StateSpellVisualID = CGObjectData.End + 196  # size 1 flags: 
    StateAnimID = CGObjectData.End + 197  # size 1 flags: 
    StateAnimKitID = CGObjectData.End + 198  # size 1 flags: 
    StateWorldEffectID = CGObjectData.End + 199  # size 4 flags: 
    ScaleDuration = CGObjectData.End + 203  # size 1 flags: MIRROR_ALL
    LooksLikeMountID = CGObjectData.End + 204  # size 1 flags: MIRROR_ALL
    LooksLikeCreatureID = CGObjectData.End + 205  # size 1 flags: MIRROR_ALL
    LookAtControllerID = CGObjectData.End + 206  # size 1 flags: MIRROR_ALL
    GuildGUID = CGObjectData.End + 207  # size 4 flags: MIRROR_ALL
    End = CGObjectData.End + 211


class CGPlayerData:
    DuelArbiter = CGUnitData.End + 0  # size 4 flags: MIRROR_ALL
    WowAccount = CGUnitData.End + 4  # size 4 flags: MIRROR_ALL
    LootTargetGUID = CGUnitData.End + 8  # size 4 flags: MIRROR_ALL
    PlayerFlags = CGUnitData.End + 12  # size 1 flags: MIRROR_ALL
    PlayerFlagsEx = CGUnitData.End + 13  # size 1 flags: MIRROR_ALL
    GuildRankID = CGUnitData.End + 14  # size 1 flags: MIRROR_ALL
    GuildDeleteDate = CGUnitData.End + 15  # size 1 flags: MIRROR_ALL
    GuildLevel = CGUnitData.End + 16  # size 1 flags: MIRROR_ALL
    HairColorID = CGUnitData.End + 17  # size 1 flags: MIRROR_ALL
    CustomDisplayOption = CGUnitData.End + 18  # size 1 flags: MIRROR_ALL
    Inebriation = CGUnitData.End + 19  # size 1 flags: MIRROR_ALL
    PvpRank = CGUnitData.End + 20  # size 1 flags: MIRROR_ALL
    DuelTeam = CGUnitData.End + 21  # size 1 flags: MIRROR_ALL
    GuildTimeStamp = CGUnitData.End + 22  # size 1 flags: MIRROR_ALL
    QuestLog = CGUnitData.End + 23  # size 320 flags: MIRROR_PARTY
    VisibleItems = CGUnitData.End + 343  # size 38 flags: MIRROR_ALL
    PlayerTitle = CGUnitData.End + 381  # size 1 flags: MIRROR_ALL
    FakeInebriation = CGUnitData.End + 382  # size 1 flags: MIRROR_ALL
    VirtualPlayerRealm = CGUnitData.End + 383  # size 1 flags: MIRROR_ALL
    CurrentSpecID = CGUnitData.End + 384  # size 1 flags: MIRROR_ALL
    TaxiMountAnimKitID = CGUnitData.End + 385  # size 1 flags: MIRROR_ALL
    AvgItemLevel = CGUnitData.End + 386  # size 4 flags: MIRROR_ALL
    CurrentBattlePetBreedQuality = CGUnitData.End + 390  # size 1 flags: MIRROR_ALL
    HonorLevel = CGUnitData.End + 391  # size 1 flags: MIRROR_ALL
    End = CGUnitData.End + 392


class CGActivePlayerData:
    InvSlots = CGPlayerData.End + 0  # size 368 flags: MIRROR_ALL
    FarsightObject = CGPlayerData.End + 368  # size 4 flags: MIRROR_ALL
    ComboTarget = CGPlayerData.End + 372  # size 4 flags: MIRROR_ALL
    SummonedBattlePetGUID = CGPlayerData.End + 376  # size 4 flags: MIRROR_ALL
    KnownTitles = CGPlayerData.End + 380  # size 12 flags: MIRROR_ALL
    Coinage = CGPlayerData.End + 392  # size 2 flags: MIRROR_ALL
    XP = CGPlayerData.End + 394  # size 1 flags: MIRROR_ALL
    NextLevelXP = CGPlayerData.End + 395  # size 1 flags: MIRROR_ALL
    TrialXP = CGPlayerData.End + 396  # size 1 flags: MIRROR_ALL
    Skill = CGPlayerData.End + 397  # size 896 flags: MIRROR_ALL
    CharacterPoints = CGPlayerData.End + 1293  # size 1 flags: MIRROR_ALL
    MaxTalentTiers = CGPlayerData.End + 1294  # size 1 flags: MIRROR_ALL
    TrackCreatureMask = CGPlayerData.End + 1295  # size 1 flags: MIRROR_ALL
    TrackResourceMask = CGPlayerData.End + 1296  # size 2 flags: MIRROR_ALL
    MainhandExpertise = CGPlayerData.End + 1298  # size 1 flags: MIRROR_ALL
    OffhandExpertise = CGPlayerData.End + 1299  # size 1 flags: MIRROR_ALL
    RangedExpertise = CGPlayerData.End + 1300  # size 1 flags: MIRROR_ALL
    CombatRatingExpertise = CGPlayerData.End + 1301  # size 1 flags: MIRROR_ALL
    BlockPercentage = CGPlayerData.End + 1302  # size 1 flags: MIRROR_ALL
    DodgePercentage = CGPlayerData.End + 1303  # size 1 flags: MIRROR_ALL
    DodgePercentageFromAttribute = CGPlayerData.End + 1304  # size 1 flags: MIRROR_ALL
    ParryPercentage = CGPlayerData.End + 1305  # size 1 flags: MIRROR_ALL
    ParryPercentageFromAttribute = CGPlayerData.End + 1306  # size 1 flags: MIRROR_ALL
    CritPercentage = CGPlayerData.End + 1307  # size 1 flags: MIRROR_ALL
    RangedCritPercentage = CGPlayerData.End + 1308  # size 1 flags: MIRROR_ALL
    OffhandCritPercentage = CGPlayerData.End + 1309  # size 1 flags: MIRROR_ALL
    SpellCritPercentage = CGPlayerData.End + 1310  # size 1 flags: MIRROR_ALL
    ShieldBlock = CGPlayerData.End + 1311  # size 1 flags: MIRROR_ALL
    Mastery = CGPlayerData.End + 1312  # size 1 flags: MIRROR_ALL
    Speed = CGPlayerData.End + 1313  # size 1 flags: MIRROR_ALL
    Avoidance = CGPlayerData.End + 1314  # size 1 flags: MIRROR_ALL
    Sturdiness = CGPlayerData.End + 1315  # size 1 flags: MIRROR_ALL
    Versatility = CGPlayerData.End + 1316  # size 1 flags: MIRROR_ALL
    VersatilityBonus = CGPlayerData.End + 1317  # size 1 flags: MIRROR_ALL
    PvpPowerDamage = CGPlayerData.End + 1318  # size 1 flags: MIRROR_ALL
    PvpPowerHealing = CGPlayerData.End + 1319  # size 1 flags: MIRROR_ALL
    ExploredZones = CGPlayerData.End + 1320  # size 320 flags: MIRROR_ALL
    RestInfo = CGPlayerData.End + 1640  # size 4 flags: MIRROR_ALL
    ModDamageDonePos = CGPlayerData.End + 1644  # size 7 flags: MIRROR_ALL
    ModDamageDoneNeg = CGPlayerData.End + 1651  # size 7 flags: MIRROR_ALL
    ModDamageDonePercent = CGPlayerData.End + 1658  # size 7 flags: MIRROR_ALL
    ModHealingDonePos = CGPlayerData.End + 1665  # size 1 flags: MIRROR_ALL
    ModHealingPercent = CGPlayerData.End + 1666  # size 1 flags: MIRROR_ALL
    ModHealingDonePercent = CGPlayerData.End + 1667  # size 1 flags: MIRROR_ALL
    ModPeriodicHealingDonePercent = CGPlayerData.End + 1668  # size 1 flags: MIRROR_ALL
    WeaponDmgMultipliers = CGPlayerData.End + 1669  # size 3 flags: MIRROR_ALL
    WeaponAtkSpeedMultipliers = CGPlayerData.End + 1672  # size 3 flags: MIRROR_ALL
    ModSpellPowerPercent = CGPlayerData.End + 1675  # size 1 flags: MIRROR_ALL
    ModResiliencePercent = CGPlayerData.End + 1676  # size 1 flags: MIRROR_ALL
    OverrideSpellPowerByAPPercent = CGPlayerData.End + 1677  # size 1 flags: MIRROR_ALL
    OverrideAPBySpellPowerPercent = CGPlayerData.End + 1678  # size 1 flags: MIRROR_ALL
    ModTargetResistance = CGPlayerData.End + 1679  # size 1 flags: MIRROR_ALL
    ModTargetPhysicalResistance = CGPlayerData.End + 1680  # size 1 flags: MIRROR_ALL
    LocalFlags = CGPlayerData.End + 1681  # size 1 flags: MIRROR_ALL
    PvpMedals = CGPlayerData.End + 1682  # size 1 flags: MIRROR_ALL
    BuybackPrice = CGPlayerData.End + 1683  # size 12 flags: MIRROR_ALL
    BuybackTimestamp = CGPlayerData.End + 1695  # size 12 flags: MIRROR_ALL
    SessionDishonorableKills = CGPlayerData.End + 1707  # size 1 flags: MIRROR_ALL
    YesterdayDishonorableKills = CGPlayerData.End + 1708  # size 1 flags: MIRROR_ALL
    LastWeekDishonorableKills = CGPlayerData.End + 1709  # size 1 flags: MIRROR_ALL
    ThisWeekDishonorableKills = CGPlayerData.End + 1710  # size 1 flags: MIRROR_ALL
    ThisWeekContribution = CGPlayerData.End + 1711  # size 1 flags: MIRROR_ALL
    LifetimeHonorableKills = CGPlayerData.End + 1712  # size 1 flags: MIRROR_ALL
    LifetimeDishonorableKills = CGPlayerData.End + 1713  # size 1 flags: MIRROR_ALL
    YesterdayContribution = CGPlayerData.End + 1714  # size 1 flags: MIRROR_ALL
    LastWeekContribution = CGPlayerData.End + 1715  # size 1 flags: MIRROR_ALL
    LastWeekRank = CGPlayerData.End + 1716  # size 1 flags: MIRROR_ALL
    WatchedFactionIndex = CGPlayerData.End + 1717  # size 1 flags: MIRROR_ALL
    CombatRatings = CGPlayerData.End + 1718  # size 32 flags: MIRROR_ALL
    PvpInfo = CGPlayerData.End + 1750  # size 54 flags: MIRROR_ALL
    MaxLevel = CGPlayerData.End + 1804  # size 1 flags: MIRROR_ALL
    ScalingPlayerLevelDelta = CGPlayerData.End + 1805  # size 1 flags: MIRROR_ALL
    MaxCreatureScalingLevel = CGPlayerData.End + 1806  # size 1 flags: MIRROR_ALL
    NoReagentCostMask = CGPlayerData.End + 1807  # size 4 flags: MIRROR_ALL
    PetSpellPower = CGPlayerData.End + 1811  # size 1 flags: MIRROR_ALL
    ProfessionSkillLine = CGPlayerData.End + 1812  # size 2 flags: MIRROR_ALL
    UiHitModifier = CGPlayerData.End + 1814  # size 1 flags: MIRROR_ALL
    UiSpellHitModifier = CGPlayerData.End + 1815  # size 1 flags: MIRROR_ALL
    HomeRealmTimeOffset = CGPlayerData.End + 1816  # size 1 flags: MIRROR_ALL
    ModPetHaste = CGPlayerData.End + 1817  # size 1 flags: MIRROR_ALL
    NumBackpackSlots = CGPlayerData.End + 1818  # size 1 flags: MIRROR_ALL
    OverrideSpellsID = CGPlayerData.End + 1819  # size 1 flags: 
    LfgBonusFactionID = CGPlayerData.End + 1820  # size 1 flags: MIRROR_ALL
    LootSpecID = CGPlayerData.End + 1821  # size 1 flags: MIRROR_ALL
    OverrideZonePVPType = CGPlayerData.End + 1822  # size 1 flags: 
    BagSlotFlags = CGPlayerData.End + 1823  # size 4 flags: MIRROR_ALL
    BankBagSlotFlags = CGPlayerData.End + 1827  # size 6 flags: MIRROR_ALL
    PvpRankProgress = CGPlayerData.End + 1833  # size 1 flags: MIRROR_ALL
    End = CGPlayerData.End + 1834


class CGGameObjectData:
    CreatedBy = CGObjectData.End + 0  # size 4 flags: MIRROR_ALL
    GuildGUID = CGObjectData.End + 4  # size 4 flags: MIRROR_ALL
    DisplayID = CGObjectData.End + 8  # size 1 flags: 
    Flags = CGObjectData.End + 9  # size 1 flags: 
    ParentRotation = CGObjectData.End + 10  # size 4 flags: MIRROR_ALL
    FactionTemplate = CGObjectData.End + 14  # size 1 flags: MIRROR_ALL
    Level = CGObjectData.End + 15  # size 1 flags: MIRROR_ALL
    PercentHealth = CGObjectData.End + 16  # size 1 flags: 
    SpellVisualID = CGObjectData.End + 17  # size 1 flags: 
    StateSpellVisualID = CGObjectData.End + 18  # size 1 flags: 
    SpawnTrackingStateAnimID = CGObjectData.End + 19  # size 1 flags: 
    SpawnTrackingStateAnimKitID = CGObjectData.End + 20  # size 1 flags: 
    StateWorldEffectID = CGObjectData.End + 21  # size 4 flags: 
    CustomParam = CGObjectData.End + 25  # size 1 flags: 
    End = CGObjectData.End + 26


class CGDynamicObjectData:
    Caster = CGObjectData.End + 0  # size 4 flags: MIRROR_ALL
    Type = CGObjectData.End + 4  # size 1 flags: MIRROR_ALL
    SpellXSpellVisualID = CGObjectData.End + 5  # size 1 flags: MIRROR_ALL
    SpellID = CGObjectData.End + 6  # size 1 flags: MIRROR_ALL
    Radius = CGObjectData.End + 7  # size 1 flags: MIRROR_ALL
    CastTime = CGObjectData.End + 8  # size 1 flags: MIRROR_ALL
    End = CGObjectData.End + 9


class CGCorpseData:
    Owner = CGObjectData.End + 0  # size 4 flags: MIRROR_ALL
    PartyGUID = CGObjectData.End + 4  # size 4 flags: MIRROR_ALL
    GuildGUID = CGObjectData.End + 8  # size 4 flags: MIRROR_ALL
    DisplayID = CGObjectData.End + 12  # size 1 flags: MIRROR_ALL
    Items = CGObjectData.End + 13  # size 19 flags: MIRROR_ALL
    SkinID = CGObjectData.End + 32  # size 1 flags: MIRROR_ALL
    FacialHairStyleID = CGObjectData.End + 33  # size 1 flags: MIRROR_ALL
    Flags = CGObjectData.End + 34  # size 1 flags: MIRROR_ALL
    DynamicFlags = CGObjectData.End + 35  # size 1 flags: MIRROR_VIEWER_DEPENDENT
    FactionTemplate = CGObjectData.End + 36  # size 1 flags: MIRROR_ALL
    CustomDisplayOption = CGObjectData.End + 37  # size 1 flags: MIRROR_ALL
    End = CGObjectData.End + 38


class CGAreaTriggerData:
    OverrideScaleCurve = CGObjectData.End + 0  # size 7 flags: 
    ExtraScaleCurve = CGObjectData.End + 7  # size 7 flags: 
    Caster = CGObjectData.End + 14  # size 4 flags: MIRROR_ALL
    Duration = CGObjectData.End + 18  # size 1 flags: MIRROR_ALL
    TimeToTarget = CGObjectData.End + 19  # size 1 flags: 
    TimeToTargetScale = CGObjectData.End + 20  # size 1 flags: 
    TimeToTargetExtraScale = CGObjectData.End + 21  # size 1 flags: 
    SpellID = CGObjectData.End + 22  # size 1 flags: MIRROR_ALL
    SpellForVisuals = CGObjectData.End + 23  # size 1 flags: MIRROR_ALL
    SpellXSpellVisualID = CGObjectData.End + 24  # size 1 flags: MIRROR_ALL
    BoundsRadius2D = CGObjectData.End + 25  # size 1 flags: 
    DecalPropertiesID = CGObjectData.End + 26  # size 1 flags: MIRROR_ALL
    CreatingEffectGUID = CGObjectData.End + 27  # size 4 flags: MIRROR_ALL
    End = CGObjectData.End + 31


class CGSceneObjectData:
    ScriptPackageID = CGObjectData.End + 0  # size 1 flags: MIRROR_ALL
    RndSeedVal = CGObjectData.End + 1  # size 1 flags: MIRROR_ALL
    CreatedBy = CGObjectData.End + 2  # size 4 flags: MIRROR_ALL
    SceneType = CGObjectData.End + 6  # size 1 flags: MIRROR_ALL
    End = CGObjectData.End + 7


class CGConversationData:
    LastLineEndTime = CGObjectData.End + 0  # size 1 flags: MIRROR_VIEWER_DEPENDENT
    End = CGObjectData.End + 1


class CGItemDynamicData:
    Modifiers = CGObjectData.End + 0  # size 4 flags: MIRROR_NONE
    BonusListIDs = CGObjectData.End + 1  # size 260 flags: MIRROR_NONE
    ArtifactPowers = CGObjectData.End + 2  # size 4 flags: MIRROR_NONE
    Gems = CGObjectData.End + 3  # size 4 flags: MIRROR_NONE
    End = CGObjectData.End + 4


class CGUnitDynamicData:
    PassiveSpells = CGObjectData.End + 0  # size 513 flags: MIRROR_NONE
    WorldEffects = CGObjectData.End + 1  # size 513 flags: MIRROR_NONE
    ChannelObjects = CGObjectData.End + 2  # size 513 flags: MIRROR_NONE
    End = CGObjectData.End + 3


class CGPlayerDynamicData:
    ArenaCooldowns = CGObjectData.End + 0  # size 1 flags: MIRROR_NONE
    End = CGObjectData.End + 1


class CGActivePlayerDynamicData:
    ResearchSites = CGObjectData.End + 0  # size 1 flags: MIRROR_NONE
    ResearchSiteProgress = CGObjectData.End + 1  # size 1 flags: MIRROR_NONE
    DailyQuestsCompleted = CGObjectData.End + 2  # size 1 flags: MIRROR_NONE
    AvailableQuestLineXQuestIDs = CGObjectData.End + 3  # size 1 flags: MIRROR_NONE
    Heirlooms = CGObjectData.End + 4  # size 1 flags: MIRROR_NONE
    HeirloomFlags = CGObjectData.End + 5  # size 1 flags: MIRROR_NONE
    Toys = CGObjectData.End + 6  # size 1 flags: MIRROR_NONE
    Transmog = CGObjectData.End + 7  # size 1 flags: MIRROR_NONE
    ConditionalTransmog = CGObjectData.End + 8  # size 1 flags: MIRROR_NONE
    SelfResSpells = CGObjectData.End + 9  # size 1 flags: MIRROR_NONE
    CharacterRestrictions = CGObjectData.End + 10  # size 1 flags: MIRROR_NONE
    SpellPctModByLabel = CGObjectData.End + 11  # size 1 flags: MIRROR_NONE
    SpellFlatModByLabel = CGObjectData.End + 12  # size 1 flags: MIRROR_NONE
    Research = CGObjectData.End + 13  # size 1 flags: MIRROR_NONE
    End = CGObjectData.End + 14


class CGGameObjectDynamicData:
    EnableDoodadSets = CGObjectData.End + 0  # size 1 flags: MIRROR_NONE
    End = CGObjectData.End + 1


class CGConversationDynamicData:
    Actors = CGObjectData.End + 0  # size 1 flags: MIRROR_NONE
    Lines = CGObjectData.End + 1  # size 256 flags: MIRROR_NONE
    End = CGObjectData.End + 2


