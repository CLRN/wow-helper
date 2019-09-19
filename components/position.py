
class Position:
    def __init__(self, x, y, z):
        self.px = x
        self.py = y
        self.pz = z

    def __str__(self):
        return f"{self.x(), self.y()}"

    def __eq__(self, other):
        return self.x() == other.x() and self.y() == other.y()

    def x(self):
        return self.px

    def y(self):
        return self.py

    def z(self):
        return None

    def r(self):
        return 0

    def id(self):
        return 0
