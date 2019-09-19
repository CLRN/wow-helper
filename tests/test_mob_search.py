from machines.mob_search import MobSearch

from unittest.mock import Mock, call


def test_search_simple():
    controller = Mock()

    calls = {"up": list(), "down": list(), "press": list()}

    machine = MobSearch(controller)
    assert machine.is_in_range

    machine.process(40, False, (100, 200), 0)
    assert machine.is_moving_to
    calls['down'].append(call('w'))

    machine.process(18, False, (100, 100), 0)
    assert machine.is_in_range
    calls['up'].append(call('w'))

    machine.process(19, False, (100, 100), 0)
    assert machine.in_range

    machine.process(19, True, (100, 100), 0)
    assert machine.is_selected

    for method, args in calls.items():
        getattr(controller, method).assert_has_calls(args)

    controller.click.assert_called_with(100, 100)

