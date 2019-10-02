from components.settings import Settings
from algos.relativity import Relativity


class MobSearch:
    def __init__(self, controller, rotation, moving):
        self.controller = controller
        self.rotation = rotation
        self.moving = moving

    def process(self, player, found_mob, target, target_coords, required_range):

        self.rotation.process(Relativity.angle(player, found_mob), required_angle=Settings.SEARCH_ANGLE_RANGE)
        self.moving.process(player, found_mob, required_range)

        if self.moving.is_staying or target_coords:
            if target and found_mob.id() == target.id():
                return True
            elif target_coords and self.rotation.is_facing:
                self.controller.click(target_coords[0], target_coords[1])
