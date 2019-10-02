from statemachine import StateMachine, State
from components.settings import Settings
from algos.relativity import Relativity
from components.position import Position

import logging


class CombatAction(StateMachine):
    attacking = State('Attacking target', initial=True)
    casting_started = State('Started casting a spell')
    casting = State('Casting a spell')

    stop = casting_started.to(attacking) | casting.to(attacking) | attacking.to(attacking)
    cast = attacking.to(casting_started) | casting_started.to(casting_started) | casting.to(casting_started)
    cast_detected = casting_started.to(casting) | attacking.to(casting) | casting.to(casting)
    casting_finished = casting.to(attacking)

    def __init__(self, controller, rotation, moving):
        self.controller = controller
        self.spell = None
        StateMachine.__init__(self)
        self.rotation = rotation
        self.moving = moving

    def process(self, player, target, next_spell, is_casting, path):
        previous_spell = self.spell
        self.spell = next_spell

        if is_casting:
            if not self.is_casting:
                self.cast_detected()
            return  # just waiting for cast to finish

        # were we casting something?
        if self.is_casting:
            self.casting_finished()
            return

        while len(path) and Relativity.distance(player, Position(path[0].x(), path[0].y())) < Settings.WAYPOINTS_MIN_DISTANCE:
            logging.info(f"Reached way point {path[0]}, remaining: {len(path) - 1}")
            path.pop(0)

        to_target = Relativity.distance(player, target)
        next_target = Position(path[0].x(), path[0].y()) if len(path) and Relativity.distance(player, path[0]) < to_target else target
        required_range = Settings.WAYPOINTS_MIN_DISTANCE if len(path) else self.spell.max_range

        self.rotation.process(Relativity.angle(player, next_target))
        self.moving.process(player, next_target, required_range)

        if self.moving.is_staying:
            if previous_spell and previous_spell.bind_key != self.spell.bind_key:
                logging.info(f"Casting spell {self.spell.bind_key}")
            self.controller.press(self.spell.bind_key)
            if self.spell.cast_time:
                self.cast()
