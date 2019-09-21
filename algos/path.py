from scipy.spatial.kdtree import KDTree
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, breadth_first_order
import numpy as np
import math
from algos.locator import Locator


def test(src, dst):
    locator = Locator()
    path = locator.known_route(locator.points[src][0], locator.points[src][1],
                               locator.points[dst][0], locator.points[dst][1])
    print([x for x in path])


if __name__ == '__main__':
    test(0, 20)

