from statemachine import StateMachine, State
import logging
import time
import random


SEARCH_RANGE = 20


class MobSearch(StateMachine):
    out_of_range = State('Standing out of range')
    moving_to = State('Moving in range distance')
    in_range = State('Mob in range to select', initial=True)
    selected = State('Selected target')

    move_closer = out_of_range.to(moving_to) | in_range.to(moving_to)
    stop = moving_to.to(in_range)
    select = in_range.to(selected)

    def __init__(self, controller):
        self.controller = controller
        StateMachine.__init__(self)

    def process(self, target_range, target_selected):
        if target_range > SEARCH_RANGE and not self.is_moving_to:
            self.move_closer()
        elif target_range < SEARCH_RANGE and self.is_moving_to:
            self.stop()
        elif self.is_in_range:
            if target_selected:
                self.select()
            else:
                logging.debug("Picking next target")
                self.controller.tab()

    def on_enter_moving_to(self):
        logging.debug("Starting moving closer")
        self.controller.down('w')

    def on_exit_moving_to(self):
        logging.debug("Stopping moving closer")
        self.controller.up('w')
