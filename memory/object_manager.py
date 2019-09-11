from constants.offsets import Offsets
from constants.enums import ObjectType
from units.object import Object
from units.item import Item
from units.unit import Unit
from units.player import Player

import logging


class ObjectManager:
    def __init__(self, process):
        self.process = process

        logging.info(f"Wow: {process.str(process.base_address + Offsets.Version, 10)}."
                     f"{process.str(process.base_address + Offsets.Build, 10)}, "
                     f"date: {process.str(process.base_address + Offsets.Date, 20)}")

        self._obj_manager = process.ptr(process.base_address + Offsets.ObjMgrPtr)
        self._object_types = {
            ObjectType.Unit: Unit,
            ObjectType.Player: Player,
            ObjectType.CurrentPlayer: Player,
        }

        self._objects = dict()

        self._player_id = process.ptr(process.base_address + Offsets.LocalPlayerGUID)

        logging.info(f"Player GUID: {self._player_id}")

    def _offsets(self):
        current = self.process.ptr(self._obj_manager + Offsets.FirstObj)

        while current:
            try:
                next_obj = self.process.ptr(current + Offsets.NextObj)
                yield current
                current = next_obj
            except:
                break

    def update(self):
        self._objects = dict()

        for offset in self._offsets():
            obj_type = self.process.byte(offset + Offsets.ObjType)
            if obj_type not in self._object_types:
                continue

            obj = self._object_types[obj_type](self.process, offset)
            self._objects[obj.id()] = obj

    def object(self, obj_id):
        return self._objects[obj_id]

    def objects(self):
        return self._objects.values()

    def player(self):
        return self._objects[self._player_id]

    def target(self):
        target_guid = self.process.ptr(self.process.base_address + Offsets.TargetGuid)
        return self._objects[target_guid] if target_guid in self._objects else None
