from statemachine import StateMachine, State

import math
import logging

ANGLE_RANGE = 30


class Rotation(StateMachine):
    facing = State('Facing', initial=True)
    left = State('Left')
    right = State('Right')

    turn_right = facing.to(right)
    turn_left = facing.to(left)
    stop_turning = left.to(facing) | right.to(facing)

    def __init__(self, controller, kiting=False):
        self.controller = controller
        self.is_kiting = kiting
        StateMachine.__init__(self)

    def process(self, angle):
        value = 180 - math.fabs(angle) if self.is_kiting else math.fabs(angle)

        if (self.is_left or self.is_right) and value < ANGLE_RANGE:
            self.stop_turning()
        elif self.is_facing and value > ANGLE_RANGE:
            if angle > 0:
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
