from components.settings import Settings
from algos.relativity import Relativity
from components.position import Position

import logging


class MobSearch:
    def __init__(self, controller, rotation, moving):
        self.controller = controller
        self.rotation = rotation
        self.moving = moving

    def process(self, player, found_mob, target, target_coords, path):

        while len(path) and Relativity.distance(player, Position(path[0].x(), path[0].y())) < Settings.WAYPOINTS_MIN_DISTANCE:
            logging.info(f"Reached way point {path[0]}, remaining: {len(path) - 1}")
            path.pop(0)

        to_target = Relativity.distance(player, found_mob)

        next_target = Position(path[0].x(), path[0].y()) if len(path) and Relativity.distance(player, path[0]) < to_target else found_mob
        distance = Relativity.distance(player, next_target)
        required_angle = Settings.SEARCH_ANGLE_RANGE if distance < Settings.SEARCH_RANGE else Settings.SEARCH_ANGLE_RANGE / 2
        required_range = Settings.WAYPOINTS_MIN_DISTANCE if len(path) else Settings.SEARCH_RANGE

        self.rotation.process(Relativity.angle(player, next_target), required_angle=required_angle)
        self.moving.process(player, next_target, required_range)

        if self.moving.is_staying or target_coords:
            if target and found_mob.id() == target.id():
                return True
            elif target_coords and self.rotation.is_facing and next_target == target:
                self.controller.click(target_coords[0], target_coords[1])
