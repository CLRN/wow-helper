from machines.moving import Moving
from components.position import Position
from components.settings import Settings

from unittest.mock import Mock, call


def test_moving_starts():
    controller = Mock()

    machine = Moving(controller)
    assert machine.is_staying

    machine.process(Position(0, 0, 0), Position(10, 10, 0), 5)
    assert machine.is_moving
    controller.down.assert_called_once_with('w')

    machine.process(Position(0, 0, 0), Position(2, 2, 0), 5)
    assert machine.is_staying
    controller.up.assert_called_once_with('w')


def test_moving_sticks():
    controller = Mock()

    machine = Moving(controller)
    assert machine.is_staying

    Settings.STUCK_CHECK_INTERVAL = 0

    calls = {"up": list(), "down": list(), "press": list()}

    machine.process(Position(0, 0, 0), Position(10, 10, 0), 5)
    assert machine.is_moving
    calls['down'].append(call('w'))

    machine.process(Position(5, 5, 0), Position(10, 10, 0), 5)
    machine.process(Position(5, 5, 0), Position(10, 10, 0), 5)
    calls['press'].append(call('space'))

    machine.process(Position(5, 5, 0), Position(10, 10, 0), 5)
    calls['up'].append(call('w'))
    assert machine.is_sticking

    machine.process(Position(5, 5, 0), Position(12, 12, 0), 5)
    assert machine.is_moving

    for method, args in calls.items():
        getattr(controller, method).assert_has_calls(args)


def test_moving_kite():
    controller = Mock()

    machine = Moving(controller, kiting=True)
    assert machine.is_staying

    machine.process(Position(0, 0), Position(0, 1), 30)
    assert machine.is_moving
    controller.down.assert_called_once_with('w')

    machine.process(Position(0, 0), Position(50, 50), 30)
    assert machine.is_staying
    controller.up.assert_called_once_with('w')
