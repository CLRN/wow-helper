from statemachine import StateMachine, State
from machines.rotation import Rotation
import logging
import time
import random


class CombatAction(StateMachine):
    out_of_range = State('Standing out of range')
    moving_to = State('Moving in range distance')
    in_range = State('Attacking in range', initial=True)
    moving_away = State('Too close to the target')
    casting_started = State('Started casting a spell')
    casting = State('Casting a spell')

    move_closer = out_of_range.to(moving_to) | moving_away.to(moving_to) | in_range.to(moving_to)
    stop = out_of_range.to(in_range) | moving_to.to(in_range) | in_range.to(in_range) | moving_away.to(in_range) | \
           casting_started.to(in_range) | casting.to(in_range)
    move_away = in_range.to(moving_away) | moving_to.to(moving_away)
    cast = moving_away.to(casting_started) | moving_to.to(casting_started) | in_range.to(casting_started) | \
           casting_started.to(casting_started)
    cast_detected = casting_started.to(casting) | moving_to.to(casting) | moving_away.to(casting) | in_range.to(casting)
    casting_finished = casting.to(in_range)

    def __init__(self, controller, rotation):
        self.controller = controller
        self.spell = None
        StateMachine.__init__(self)
        self.rotation = rotation
        self.last_jump = 0

    def process(self, target_range, angle, next_spell, is_casting):
        self.rotation.process(angle)

        previous_spell = self.spell
        self.spell = next_spell

        if is_casting:
            if not self.is_casting:
                self.cast_detected()
            return  # just waiting for cast to finish

        # were we casting something?
        if self.is_casting:
            self.casting_finished()

        if target_range > self.spell.max_range and not self.is_moving_to:
            self.move_closer()
        elif target_range < self.spell.min_range and not self.is_moving_away:
            self.move_away()
        elif target_range < self.spell.max_range:
            if self.is_moving_to or self.is_moving_away:
                self.stop()
            elif not self.is_casting:
                if previous_spell and previous_spell.bind_key != self.spell.bind_key:
                    logging.info(f"Casting spell {self.spell.bind_key}")
                self.controller.press(self.spell.bind_key)
                if self.spell.cast_time:
                    self.cast()
        elif self.is_moving_to and time.time() - self.last_jump > random.randint(3, 10):
            self.controller.press('space')
            self.last_jump = time.time()

    def on_enter_moving_to(self):
        logging.debug("Starting moving closer")
        self.controller.down('w')

    def on_exit_moving_to(self):
        logging.debug("Stopping moving closer")
        self.controller.up('w')

    def on_enter_moving_away(self):
        logging.debug("Starting moving away")
        self.controller.down('s')

    def on_exit_moving_away(self):
        logging.debug("Stopping moving away")
        self.controller.up('s')
