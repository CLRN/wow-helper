from statemachine import StateMachine, State
from components.settings import Settings
from components.position import Position
from algos.relativity import Relativity


import time
import logging
import random


class Moving(StateMachine):
    staying = State('Staying', initial=True)
    moving = State('Moving')
    sticking = State('Stuck')

    move = staying.to(moving) | sticking.to(moving)
    stop = sticking.to(staying) | moving.to(staying) | staying.to(staying)
    stuck = moving.to(sticking)

    def __init__(self, controller):
        self.controller = controller
        self.is_kiting = False

        StateMachine.__init__(self)

        self.last_check_time = 0
        self.last_jump = 0
        self.last_positions = list()
        self.last_target_stuck = None
        self.jump_interval = random.randint(5, 10)

    def process(self, position, target, required_range):
        distance = Relativity.distance(position, target)
        diff = required_range - distance if self.is_kiting else distance - required_range
        target_pos = Position(target.x(), target.y())

        if self.is_staying and diff > 0:
            self.move()
            logging.info(f"Moving to {target}, distance: {distance}")
        elif self.is_moving:
            if diff < 0:
                self.stop()
                return

            # detect if we got stuck
            now = time.time()
            last_check_time = self.last_check_time
            if now - last_check_time < Settings.STUCK_CHECK_INTERVAL:
                return

            self.last_check_time = now

            self.last_positions.append(Position(position.x(), position.y()))
            if len(self.last_positions) > 10:
                self.last_positions.pop(0)
            if len(self.last_positions) < 2:
                return

            if Relativity.distance(self.last_positions[-2], self.last_positions[-1]) < Settings.STUCK_CHECK_RANGE:
                if self.last_jump != last_check_time:
                    logging.warning(f"Looks like we're getting stuck, jumping! Last positions: {self.last_positions}")
                    self.last_jump = now
                    self.controller.press('space')
                else:
                    logging.warning(f"We've got stuck, jump didn't help. Last positions: {self.last_positions}")
                    self.last_target_stuck = target_pos
                    self.stuck()
            elif time.time() - self.last_jump > self.jump_interval:
                self.controller.press('space')
                self.last_jump = time.time()
                self.jump_interval = random.randint(5, 10)
        elif self.is_sticking and not target.id():  # id not set means that this is a generated WP based on mmaps
            logging.info(f"Unstuck with new next target: {target}")
            self.move()

    def on_enter_moving(self):
        logging.debug("Moving forward")
        self.controller.down('w')

    def on_exit_moving(self):
        logging.debug("Stopping moving forward")
        self.controller.up('w')

    def on_enter_sticking(self):
        logging.info(f"Stuck at {self.last_positions[-1]} when moving to {self.last_target_stuck}")
