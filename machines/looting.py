from components.settings import Settings
from algos.relativity import Relativity
import logging


class MobLooting:
    def __init__(self, controller, rotation, moving):
        self.controller = controller
        self.rotation = rotation
        self.moving = moving

    def process(self, player, target, target_coords, path):
        angle = Relativity.angle(player, target)
        if self.rotation.process(angle) and self.moving.is_staying:
            return

        self.moving.process(player, target, Settings.LOOTING_RANGE)
        if self.moving.is_staying and target_coords:
            logging.debug(f"Looting target, coords: {target_coords}")
            self.controller.click(target_coords[0], target_coords[1])
