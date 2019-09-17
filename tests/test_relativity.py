from algos.relativity import Relativity
from unittest.mock import Mock, call
from components.position import Position
from components.settings import Settings

import math


def test_angle():
    mob1 = Position(0, 0, 0)
    mob2 = Position(10, 10, 0)

    assert Relativity.angle(mob1, mob2) == math.radians(45)


def test_distance():
    mob1 = Position(0, 0, 0)
    mob2 = Position(1, 1, 0)

    assert Relativity.distance(mob1, mob2) == math.sqrt(2)


def test_direct_path():
    x = 123
    y = 321

    mob1 = Position(0, 0, 0)
    mob2 = Position(x, y, 0)

    total = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    r = Relativity.direct_route(mob1, mob2)
    assert len(r) == int(total / Settings.WAYPOINTS_MIN_DISTANCE)