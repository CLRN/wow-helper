from constants.manual_offsets import Location, ObjectOffsets
from components.position import Position


class Object:
    def __init__(self, process, offset):
        self.process = process
        self.offset = offset
        self.descriptors = self.process.ptr(offset + ObjectOffsets.Descriptors)

    def id(self):
        return self.process.ptr(self.offset + ObjectOffsets.ObjGUID)

    def type(self):
        return self.process.byte(self.offset + ObjectOffsets.ObjType)

    def position(self):
        return Position(self.x(), self.y(), self.z())

    def x(self):
        return self.process.float(self.offset + ObjectOffsets.UnitPosition + Location.X)

    def y(self):
        return self.process.float(self.offset + ObjectOffsets.UnitPosition + Location.Y)

    def z(self):
        return self.process.float(self.offset + ObjectOffsets.UnitPosition + Location.Z)

    def r(self):
        return self.process.float(self.offset + ObjectOffsets.UnitPosition + Location.R)

    def __repr__(self):
        public = [method_name for method_name in dir(self) if not method_name.startswith("__")]
        methods = [method_name for method_name in public if callable(getattr(self, method_name))]
        return ", ".join([f"{name}: {getattr(self, name)()}" for name in methods])

    def __str__(self):
        return self.__repr__()
