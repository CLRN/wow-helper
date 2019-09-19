from machines.mob_search import MobSearch
from components.position import Position

from unittest.mock import Mock, call


def test_search_simple():
    controller = Mock()
    rotation = Mock()
    moving = Mock()
    target = Mock()

    machine = MobSearch(controller, rotation, moving)

    target.id.side_effect = [123, 0]  # not equal to player, equal to player id
    target.x.side_effect = lambda: 10
    target.y.side_effect = lambda: 10

    # clicking to select target
    assert not machine.process(Position(0, 0), target, (100, 100))
    controller.click.assert_called_with(100, 100)

    # target selected
    assert machine.process(Position(0, 0), target, (100, 100))



