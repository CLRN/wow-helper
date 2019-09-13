from constants.offsets import Offsets


def get_matrix(process):
    struct = process.ptr(process.base_address + Offsets.CameraBase)
    offset = process.ptr(struct + Offsets.CameraOffset)
    # matrix = process.ptr(offset + Offsets.CameraMatrix)

    result = [[0 for x in range(3)] for y in range(3)]
    for row in range(0, 2):
        for col in range(0, 2):
            result[row][col] = process.float(offset + Offsets.CameraMatrix + (row * 3 + col) * 4)

    return result


def get_position():
    pass

def get_fov():
    pass