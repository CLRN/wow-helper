from statemachine import StateMachine, State
from components.settings import Settings

import math
import logging


class Rotation(StateMachine):
    facing = State('Facing', initial=True)
    left = State('Left')
    right = State('Right')

    turn_right = facing.to(right)
    turn_left = facing.to(left)
    stop_turning = left.to(facing) | right.to(facing) | facing.to(facing)

    def __init__(self, controller, kiting=False):
        self.controller = controller
        self.is_kiting = kiting
        StateMachine.__init__(self)

    def process(self, angle_radians, required_angle=Settings.ATTACK_ANGLE_RANGE):
        degrees = 180 - math.degrees(angle_radians) if self.is_kiting else math.degrees(angle_radians)

        if (self.is_left or self.is_right) and math.fabs(degrees) < required_angle:
            self.stop_turning()
        elif self.is_facing and math.fabs(degrees) > required_angle:
            logging.info(f"Rotating to {angle_radians}")
            if angle_radians > 0:
                self.turn_left()
            else:
                self.turn_right()

    def on_enter_left(self):
        logging.debug("Turning left")
        self.controller.down('a')

    def on_exit_left(self):
        logging.debug("Stopping turning left")
        self.controller.up('a')

    def on_enter_right(self):
        logging.debug("Turning right")
        self.controller.down('d')

    def on_exit_right(self):
        logging.debug("Stopping turning right")
        self.controller.up('d')
