from components.settings import Settings
from algos.relativity import Relativity


class MobSearch:
    def __init__(self, controller, rotation, moving):
        self.controller = controller
        self.rotation = rotation
        self.moving = moving

    def process(self, player, target, target_coords):
        self.rotation.process(Relativity.angle(player, target))
        self.moving.process(player, target, Settings.SEARCH_RANGE)

        if self.moving.is_staying or target_coords:
            if player.id() == target.id():
                return True
            elif target_coords and self.rotation.is_facing:
                self.controller.click(target_coords[0], target_coords[1])
