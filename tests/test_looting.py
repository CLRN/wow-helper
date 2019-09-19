from machines.looting import MobLooting
from components.position import Position

from unittest.mock import Mock, call


def test_looting_simple():
    controller = Mock()
    rotation = Mock()
    moving = Mock()

    machine = MobLooting(controller, rotation, moving)

    rotation.process.side_effect = lambda x: False
    moving.is_staying.side_effect = True

    machine.process(Position(0, 0), Position(1, 1), (100, 100))

    controller.click.assert_called_once_with(100, 100)
