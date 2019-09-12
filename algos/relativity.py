import math


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
