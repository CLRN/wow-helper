class Global:
    FirstObj = 0x18
    NextObj = 0x40


class Camera:
    CameraOffset = 0x3330
    CameraOrigin = 0x10
    CameraMatrix = 0x1C
    CameraFoV = 0x40


class Location:
    X = 0
    Y = 4
    Z = 8
    R = 16


class ObjectOffsets:
    Descriptors = 0x10
    UnitPosition = 0x1600
    ObjType = 0x20
    ObjGUID = 0x58

    CurrentSpellId = 0x1968
    IsAttacking = 0x18A4

    FirstAuraOffset = 0x1B58
    NextAuraOffset = 0xA8
