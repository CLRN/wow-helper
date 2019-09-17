from components.settings import Settings

from scipy.spatial.kdtree import KDTree
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
        self.tree = KDTree(self.points)

    def track(self, x, y):
        distance, _ = self.tree.query([x, y], distance_upper_bound=Settings.WAYPOINTS_MIN_DISTANCE)
        if distance == np.inf:
            self.points.append([x, y])
            self.output_file.write(f"{x},{y}\n")
            self.tree = KDTree(self.points)

    def known_route(self):
        return list()