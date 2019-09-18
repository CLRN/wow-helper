from statemachine import StateMachine, State
from components.settings import Settings
from machines.rotation import Rotation
import logging
import random
import time
import math


class MobSearch(StateMachine):
    out_of_range = State('Standing out of range')
    moving_to = State('Moving in range distance')
    in_range = State('Mob in range to select', initial=True)
    selected = State('Selected target')

    move_closer = out_of_range.to(moving_to) | in_range.to(moving_to)
    stop = moving_to.to(in_range) | out_of_range.to(in_range) | in_range.to(in_range) | selected.to(in_range)
    select = in_range.to(selected) | moving_to.to(selected)

    def __init__(self, controller, rotation):
        self.controller = controller
        StateMachine.__init__(self)
        self.last_jump = 0
        self.rotation = rotation

    def inactive(self):
        self.stop()

    def active(self, target_range, target_selected, target_coords, angle):
        self.rotation.process(angle, Settings.SEARCH_ANGLE_RANGE)
        if target_range > Settings.SEARCH_RANGE and not self.is_moving_to:
            self.move_closer()
        elif target_range < Settings.SEARCH_RANGE and self.is_moving_to:
            self.stop()
        elif self.is_in_range or target_coords:
            if target_selected:
                self.select()
                return True
            elif target_coords and math.fabs(angle) < Settings.SEARCH_ANGLE_RANGE:
                # logging.debug(f"Picking target, range: {target_range}, coords: {target_coords}")
                self.controller.click(target_coords[0], target_coords[1])
        else:
            if time.time() - self.last_jump > random.randint(5, 10):
                self.controller.press('space')
                self.last_jump = time.time()

    def on_enter_moving_to(self):
        logging.debug("Starting moving closer")
        self.controller.down('w')

    def on_exit_moving_to(self):
        logging.debug("Stopping moving closer")
        self.controller.up('w')
