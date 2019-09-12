from machines.rotation import Rotation
import math
from unittest.mock import Mock, call


def test_init_facing():
    controller = Mock()

    machine = Rotation(controller)
    machine.process(math.radians(10))

    assert machine.is_facing

    controller.assert_not_called()


def test_init_not_facing_left():
    controller = Mock()

    machine = Rotation(controller)
    machine.process(math.radians(60))

    assert machine.is_left

    controller.down.assert_called_once_with('a')


def test_init_not_facing_right():
    controller = Mock()

    machine = Rotation(controller)
    machine.process(math.radians(-60))

    assert machine.is_right

    controller.down.assert_called_once_with('d')


def test_full_rotation():
    controller = Mock()

    machine = Rotation(controller)
    machine.process(math.radians(100))

    # turn left
    assert not machine.is_facing
    machine.process(math.radians(70))
    machine.process(math.radians(40))
    machine.process(math.radians(20))

    controller.down.assert_called_once_with('a')
    controller.up.assert_called_once_with('a')

    # turn right
    machine.process(math.radians(-90))

    assert not machine.is_facing
    machine.process(math.radians(-10))

    calls = [call('a'), call('d')]
    controller.down.assert_has_calls(calls)
    controller.up.assert_has_calls(calls)


def test_init_kiting():
    controller = Mock()

    machine = Rotation(controller, kiting=True)
    machine.process(math.radians(10))

    assert machine.is_left

    controller.down.assert_called_once_with('a')
