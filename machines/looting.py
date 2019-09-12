from statemachine import StateMachine, State
from components.settings import Settings
import logging


class MobLooting(StateMachine):
    out_of_range = State('Standing out of range')
    moving_to = State('Moving in range distance')
    in_range = State('Mob in range to select', initial=True)
    looted = State('Looted target')

    move_closer = out_of_range.to(moving_to) | in_range.to(moving_to) | looted.to(moving_to)
    stop = moving_to.to(in_range)
    loot = in_range.to(looted)

    def __init__(self, controller):
        self.controller = controller
        StateMachine.__init__(self)

    def process(self, target_range):
        if target_range > Settings.LOOTING_RANGE and not self.is_moving_to:
            self.move_closer()
        elif target_range < Settings.LOOTING_RANGE and self.is_moving_to:
            self.stop()
        elif self.is_in_range:
            logging.debug("Looting target")
            self.controller.loot()
            self.loot()

    def on_enter_moving_to(self):
        logging.debug("Starting moving closer")
        self.controller.down('w')

    def on_exit_moving_to(self):
        logging.debug("Stopping moving closer")
        self.controller.up('w')
