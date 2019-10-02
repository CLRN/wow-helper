from algos.relativity import Relativity
from components.position import Position
from components.settings import Settings

import logging


class PathTracker:
    def __init__(self, target, path, required_range):
        self.target = target
        self.path = path
        self.required_range = required_range

        logging.info(f"Target: {self.target}, range: {required_range}, path: {self.path}")

    def _within_wp_reach(self, position):
        distance = Relativity.distance(position, Position(self.path[0].x(), self.path[0].y()))
        return distance < Settings.WAYPOINTS_MIN_DISTANCE

    def next(self, current_position):
        if not self.target:
            return None, None

        while len(self.path) and self._within_wp_reach(current_position):
            logging.info(f"Reached way point {self.path[0]}, remaining: {len(self.path) - 1}")
            self.path.pop(0)

        to_target = Relativity.distance(current_position, self.target)
        if len(self.path) and Relativity.distance(current_position, self.path[0]) < to_target:
            target = Position(self.path[0].x(), self.path[0].y())
        else:
            target = self.target

        required_range = Settings.WAYPOINTS_MIN_DISTANCE if len(self.path) else self.required_range
        return target, required_range
