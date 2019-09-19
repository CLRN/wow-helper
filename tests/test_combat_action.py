from machines.combat_action import CombatAction
from components.spell import Spell
from components.position import Position

from unittest.mock import Mock

smite_spell = Spell(0, 2, 25, 2, '2', 0)


def test_combat_simple():
    controller = Mock()
    rotation = Mock()
    moving = Mock()

    machine = CombatAction(controller, rotation, moving)
    assert machine.is_attacking

    machine.process(Position(0, 0), Position(0, 10), smite_spell, False)
    assert machine.is_casting_started

    machine.process(Position(0, 0), Position(0, 10), smite_spell, True)
    assert machine.is_casting

    machine.process(Position(0, 0), Position(0, 10), smite_spell, False)
    assert machine.is_attacking

    rotation.process.assert_called()
    moving.process.assert_called()

