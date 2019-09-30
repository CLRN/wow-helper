import _recast as dt


def test_sample_tile_mesh():
    print("Create NavMesh Object From File")
    nav_mesh = dt.dtLoadSampleTileMesh(r"c:\wow\maps_2.4.3\built\all_tiles_navmesh.bin")
    filter = dt.dtQueryFilter()
    query = dt.dtNavMeshQuery()

    print("Init NavMesh Object")
    status = query.init(nav_mesh, 2048)
    if dt.dtStatusFailed(status):
        return -1, status

    print("Fix The Input Data")
    polyPickExt = dt.dtVec3(7.0, 7.0, 7.0)
    startPos = dt.dtVec3(2320.594482421875, -2527.936279296875, 101.45013427734375)
    endPos = dt.dtVec3(2300.594482421875, -2547.936279296875, 101.45013427734375)

    status, out = query.findNearestPoly(startPos, polyPickExt, filter)
    if dt.dtStatusFailed(status):
        return -2, status
    startRef = out["nearestRef"]
    _startPt = out["nearestPt"]

    status, out = query.findNearestPoly(endPos, polyPickExt, filter)
    if dt.dtStatusFailed(status):
        return -3, status
    endRef = out["nearestRef"]
    _endPt = out["nearestPt"]

    print("Get Path Reference List")
    status, out = query.findPath(startRef, endRef, startPos, endPos, filter, 32)
    if dt.dtStatusFailed(status):
        return -4, status
    pathRefs = out["path"]

    status, fixEndPos = query.closestPointOnPoly(pathRefs[-1], endPos)
    if dt.dtStatusFailed(status):
        return -5, status

    print("Get Path Point List")
    status, out = query.findStraightPath(startPos, fixEndPos, pathRefs, 32, 0)
    if dt.dtStatusFailed(status):
        return -6, status
    straightPath = out["straightPath"]
    straightPathFlags = out["straightPathFlags"]
    straightPathRefs = out["straightPathRefs"]

    print("Print Search Result")
    print("The input data:")
    print("\tstart pos: %s" % startPos)
    print("\tend pos: %s" % endPos)

    print("The fixed input data:")
    print("\tstart point(in poly): %s" % _startPt)
    print("\tend pos(in poly): %s" % _endPt)
    print("\tend pos(fixed): %s" % fixEndPos)

    print("The final output path:")
    print("\tstraight path: %s" % straightPath)
    print("\tstraight path flags: %s" % straightPathFlags)
    print("\tstraight path refs: %s" % straightPathRefs)
    return 0, 0


def main():
    rv, st = test_sample_tile_mesh()
    print("rv=%d, st=%d" % (rv, st))


if __name__ == '__main__':
    main()
