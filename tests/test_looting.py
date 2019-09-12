from machines.looting import MobLooting

from unittest.mock import Mock, call


def test_looting_simple():
    controller = Mock()

    calls = {"up": list(), "down": list(), "press": list()}

    machine = MobLooting(controller)
    assert machine.is_in_range

    machine.process(40)
    assert machine.is_moving_to
    calls['down'].append(call('w'))

    machine.process(1)
    assert machine.is_in_range
    calls['up'].append(call('w'))

    machine.process(1)
    assert machine.is_looted

    for method, args in calls.items():
        getattr(controller, method).assert_has_calls(args)

    controller.loot.assert_called_once()

