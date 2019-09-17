from machines.looting import MobLooting

from unittest.mock import Mock, call


def test_looting_simple():
    controller = Mock()

    calls = {"up": list(), "down": list(), "press": list()}

    machine = MobLooting(controller)
    assert machine.is_in_range

    machine.active(40, (100, 100), 0)
    assert machine.is_moving_to
    calls['down'].append(call('w'))

    machine.active(1, (100, 100), 0)
    assert machine.is_in_range
    calls['up'].append(call('w'))

    machine.active(1, (100, 100), 0)
    assert machine.is_in_range

    for method, args in calls.items():
        getattr(controller, method).assert_has_calls(args)

    controller.click.assert_called_once_with(100, 100)

