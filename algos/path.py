import _recast as dt
from components.position import Position

SIZE_OF_GRIDS = 533.33333


class PathBuilder:
    def __init__(self, map_id=1):
        self.map_id = map_id
        self.maps = dt.MMapManager("f:\\tmp\\wow_3.3.5\\")
        self.filter = dt.dtQueryFilter()
        self.query = dt.dtNavMeshQuery()
        self.poly_pick_ext = dt.dtVec3(7.0, 7.0, 7.0)
        self.loaded_tiles = list()
        self.nav_mesh = None

    def _create_mesh(self):
        if self.nav_mesh:
            return

        self.nav_mesh = self.maps.mesh(self.map_id)
        if dt.dtStatusFailed(self.query.init(self.nav_mesh, 2048)):
            raise Exception(f"Unable to init query {self.map_id}")

    def _find_point(self, point):
        gx = int(32 - point.x() / SIZE_OF_GRIDS)
        gy = int(32 - point.y() / SIZE_OF_GRIDS)

        if (gx, gy) not in self.loaded_tiles:
            if not self.maps.load(1, gx, gy):
                raise Exception(f"Failed to load tile {gx}:{gy} using {point}")
            self.loaded_tiles.append((gx, gy))

        self._create_mesh()

        pos = dt.dtVec3(point.y(), point.z(), point.x())
        status, out = self.query.findNearestPoly(pos, self.poly_pick_ext, self.filter)
        if dt.dtStatusFailed(status):
            raise Exception(f"Failed to find point {point} on mesh")
        return pos, out["nearestRef"]

    def _ref_to_point(self, ref):
        coords = dt.dtVec3()
        status, pos = self.query.closestPointOnPoly(ref, coords)
        if dt.dtStatusFailed(status):
            raise Exception(f"Unable to locate poly ref {ref}")
        return Position(pos.z, pos.x, pos.y)

    def build(self, from_point, to_point):
        pos_from, from_ref = self._find_point(from_point)
        pos_to, to_ref = self._find_point(to_point)

        status, out = self.query.findPath(from_ref, to_ref, pos_from, pos_to, self.filter, 256)
        if dt.dtStatusFailed(status):
            raise Exception(f"Unable to build path from {from_ref} to {to_ref}")

        result = list()
        for point in [self._ref_to_point(x) for x in out["path"]]:
            if len(result) and result[-1] == point:
                continue
            result.append(point)

        return result


if __name__ == '__main__':
    builder = PathBuilder(1)
    res = builder.build(Position(1555.043212890625, -4421.5478515625, 8.577301979064941),
                        Position(1670.45361328125, -4413.26025390625, 18.072647094726562))
    print(res)
