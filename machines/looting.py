from statemachine import StateMachine, State
from machines.rotation import Rotation
from components.settings import Settings
import logging
import time


class MobLooting(StateMachine):
    out_of_range = State('Standing out of range')
    moving_to = State('Moving in range distance')
    in_range = State('Mob in range to select', initial=True)
    looted = State('Looted target')

    move_closer = out_of_range.to(moving_to) | in_range.to(moving_to) | looted.to(moving_to)
    stop = moving_to.to(in_range) | in_range.to(in_range) | looted.to(in_range) | out_of_range.to(in_range)
    loot = in_range.to(looted)

    def __init__(self, controller):
        self.controller = controller
        StateMachine.__init__(self)
        self.last_looting_time = 0
        self.rotation = Rotation(controller)

    def inactive(self):
        self.stop()
        self.rotation.stop_turning()

    def active(self, target_range, target_coords, target_angle):
        if self.rotation.process(target_angle) and self.is_in_range:
            return

        if target_range > Settings.LOOTING_RANGE and not self.is_moving_to:
            self.move_closer()
        elif target_range < Settings.LOOTING_RANGE and self.is_moving_to:
            self.stop()
        elif self.is_in_range and target_coords and time.time() - self.last_looting_time > Settings.LOOT_ACTION_REPEAT_SECONDS:
            logging.debug(f"Looting target. range: {target_range}, coords: {target_coords}")
            self.controller.click(target_coords[0], target_coords[1])
            self.last_looting_time = time.time()

    def on_enter_moving_to(self):
        logging.debug("Starting moving closer")
        self.controller.down('w')

    def on_exit_moving_to(self):
        logging.debug("Stopping moving closer")
        self.controller.up('w')
