from constants.offsets import Offsets
from constants.manual_offsets import Camera

import math


def get_matrix(process):
    struct = process.ptr(process.base_address + Offsets.CameraBase)
    offset = process.ptr(struct + Camera.CameraOffset)

    result = [[0 for x in range(3)] for y in range(3)]
    for row in range(3):
        for col in range(3):
            result[row][col] = process.float(offset + Camera.CameraMatrix + (row * 3 + col) * 4)

    return result


def get_position(process):
    struct = process.ptr(process.base_address + Offsets.CameraBase)
    offset = process.ptr(struct + Camera.CameraOffset)
    result = list()
    for i in range(3):
        result.append(process.float(offset + Camera.CameraOrigin + i * 4))
    return result


def get_fov(process):
    struct = process.ptr(process.base_address + Offsets.CameraBase)
    offset = process.ptr(struct + Camera.CameraOffset)
    return process.float(offset + Camera.CameraFoV)


def world_to_screen(process, window, x, y, z):
    fDiff = [float() for x in range(3)]
    fInv = [[float() for x in range(3)] for y in range(3)]
    fCam = [float() for x in range(3)]
    fView = [float() for x in range(3)]

    fViewMat = get_matrix(process)
    fCamPos = get_position(process)
    fFov = get_fov(process)

    fDiff[0] = x - fCamPos[0]
    fDiff[1] = y - fCamPos[1]
    fDiff[2] = z - fCamPos[2]

    fProd = fDiff[0] * fViewMat[0][0] + fDiff[1] * fViewMat[0][1] + fDiff[2] * fViewMat[0][2]
    if fProd < 0:
        return None

    fInv[0][0] = fViewMat[1][1] * fViewMat[2][2] - fViewMat[1][2] * fViewMat[2][1]
    fInv[1][0] = fViewMat[1][2] * fViewMat[2][0] - fViewMat[1][0] * fViewMat[2][2]
    fInv[2][0] = fViewMat[1][0] * fViewMat[2][1] - fViewMat[1][1] * fViewMat[2][0]
    fDet = fViewMat[0][0] * fInv[0][0] + fViewMat[0][1] * fInv[1][0] + fViewMat[0][2] * fInv[2][0]
    fInvDet = 1.0 / fDet
    fInv[0][1] = fViewMat[0][2] * fViewMat[2][1] - fViewMat[0][1] * fViewMat[2][2]
    fInv[0][2] = fViewMat[0][1] * fViewMat[1][2] - fViewMat[0][2] * fViewMat[1][1]
    fInv[1][1] = fViewMat[0][0] * fViewMat[2][2] - fViewMat[0][2] * fViewMat[2][0]
    fInv[1][2] = fViewMat[0][2] * fViewMat[1][0] - fViewMat[0][0] * fViewMat[1][2]
    fInv[2][1] = fViewMat[0][1] * fViewMat[2][0] - fViewMat[0][0] * fViewMat[2][1]
    fInv[2][2] = fViewMat[0][0] * fViewMat[1][1] - fViewMat[0][1] * fViewMat[1][0]
    fViewMat[0][0] = fInv[0][0] * fInvDet
    fViewMat[0][1] = fInv[0][1] * fInvDet
    fViewMat[0][2] = fInv[0][2] * fInvDet
    fViewMat[1][0] = fInv[1][0] * fInvDet
    fViewMat[1][1] = fInv[1][1] * fInvDet
    fViewMat[1][2] = fInv[1][2] * fInvDet
    fViewMat[2][0] = fInv[2][0] * fInvDet
    fViewMat[2][1] = fInv[2][1] * fInvDet
    fViewMat[2][2] = fInv[2][2] * fInvDet

    fView[0] = fInv[0][0] * fDiff[0] + fInv[1][0] * fDiff[1] + fInv[2][0] * fDiff[2]
    fView[1] = fInv[0][1] * fDiff[0] + fInv[1][1] * fDiff[1] + fInv[2][1] * fDiff[2]
    fView[2] = fInv[0][2] * fDiff[0] + fInv[1][2] * fDiff[1] + fInv[2][2] * fDiff[2]

    fCam[0] = -fView[1]
    fCam[1] = -fView[2]
    fCam[2] = fView[0]

    rect = window.rect()
    width = rect.bottom_right[0] - rect.left_top[0]
    height = rect.bottom_right[1] - rect.left_top[1]

    fScreenX = width / 2.0
    fScreenY = height / 2.0

    modifier = 1.0
    modifier2 = 1.08
    if width / height > 1.5:
        modifier *= 1.15
        modifier2 = 1.0

    fHorizontalAdjust = 48.0 if width / height >= 1.6 else 44.0

    deg2Rad = math.pi / 180

    fTmpX = fScreenX / math.tan(((fFov * fHorizontalAdjust) * modifier2 * modifier / 2.0) * deg2Rad)
    fTmpY = fScreenY / math.tan(((fFov * 35) / 2.0) * deg2Rad)

    X = fScreenX + fCam[0] * fTmpX / fCam[2]
    Y = fScreenY + fCam[1] * fTmpY / fCam[2]

    # adjust Y to point to the middle of the model
    Y -= 20

    result = window.client_to_screen(int(X), int(Y))
    if result[0] <= rect.left_top[0] or \
       result[0] >= rect.bottom_right[0] or \
       result[1] <= rect.left_top[1] or \
       result[1] >= rect.bottom_right[1]:
        return None

    return result

