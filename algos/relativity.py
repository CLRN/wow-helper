import math
from components.settings import Settings


class Relativity:
    @staticmethod
    def angle(unit1, unit2):
        radians = math.atan2(unit2.y() - unit1.y(), unit2.x() - unit1.x()) + math.radians(180)
        diff = radians - unit1.r()
        sign = 1 if diff < 0 else -1
        diff += math.radians(180) * sign
        return diff

    @staticmethod
    def distance(unit1, unit2):
        return math.sqrt(math.pow(unit2.y() - unit1.y(), 2) + math.pow(unit2.x() - unit1.x(), 2))

    @staticmethod
    def direct_route(unit1, unit2):
        angle = math.atan2(unit2.y() - unit1.y(), unit2.x() - unit1.x())

        current = [unit1.x(), unit1.y()]
        result = list()

        while math.sqrt(math.pow(unit2.y() - current[1], 2) + math.pow(unit2.x() - current[0], 2)) > Settings.WAYPOINTS_MIN_DISTANCE:
            current[0] += math.cos(angle) * Settings.WAYPOINTS_MIN_DISTANCE
            current[1] += math.sin(angle) * Settings.WAYPOINTS_MIN_DISTANCE
            result.append([current[0], current[1]])

        return result