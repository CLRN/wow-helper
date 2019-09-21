from components.settings import Settings
from components.position import Position

from scipy.spatial.kdtree import KDTree
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

import numpy as np

import os


class Locator:
    def __init__(self, file_name=Settings.WAYPOINTS_FILE):
        self.points = list()
        if os.path.exists(file_name):
            with open(file_name, 'r') as data:
                for line in data:
                    parts = line.split(',')
                    self.points.append([float(parts[0]), float(parts[1])])

        self.output_file = open(file_name, 'a')

        self.tree = KDTree(self.points) if len(self.points) else None

    def track(self, x, y):
        distance = np.inf
        if self.tree:
            distance, _ = self.tree.query([x, y], distance_upper_bound=Settings.WAYPOINTS_MIN_DISTANCE)
        if distance == np.inf:
            self.points.append([x, y])
            self.tree = KDTree(self.points)
            self.output_file.write(f"{x},{y}\n")
            self.output_file.flush()

    def closest_wp(self, x, y):
        distance, indexes = self.tree.query([x, y], k=2)
        for index in indexes:
            if self.points[index][0] != x or self.points[indexes][1] != y:
                return Position(self.points[index][0], self.points[index][1])
        return None

    def known_route(self, src_x, src_y, dst_x, dst_y):
        _, src_index = self.tree.query([src_x, src_y])
        _, dst_index = self.tree.query([dst_x, dst_y])

        pairs = self.tree.query_pairs(Settings.WAYPOINTS_MIN_DISTANCE * 2)

        arr = np.zeros((len(pairs), len(pairs)))

        for p in pairs:
            arr[p[0], p[1]] = 1

        graph = csr_matrix(arr)

        dist_matrix, predecessors = shortest_path(csgraph=graph,
                                                  directed=False,
                                                  indices=src_index,
                                                  return_predecessors=True)
        current = dst_index

        path = list()
        while current != src_index:
            next_index = predecessors[current]
            path.append(self.points[next_index])
            current = next_index

        return [x for x in reversed(path)]
