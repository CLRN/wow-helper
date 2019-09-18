from constants.offsets import Offsets
from constants.manual_offsets import Global, ObjectOffsets
from constants.enums import ObjectType
from units.object import Object
from units.item import Item
from units.unit import Unit
from units.player import Player

import logging


class ObjectManager:
    def __init__(self, process):
        self.process = process

        logging.info(f"Wow: {process.str(process.base_address + Offsets.GameVersion, 10)}."
                     f"{process.str(process.base_address + Offsets.GameBuild, 10)}, "
                     f"date: {process.str(process.base_address + Offsets.GameReleaseDate, 20)}")

        self._obj_manager = process.ptr(process.base_address + Offsets.ObjectMgrPtr)
        self._object_types = {
            ObjectType.Unit: Unit,
            ObjectType.Player: Player,
            ObjectType.CurrentPlayer: Player,
        }

        self._objects = dict()

        self._player_id = process.ptr(process.base_address + Offsets.LocalPlayerGUID)
        self.player_name = process.str(process.base_address + Global.PlayerName, 30)

        logging.info(f"Player GUID: {self._player_id}, name: {self.player_name}")

        self.update()

    def _offsets(self):
        current = self.process.ptr(self._obj_manager + Global.FirstObj)

        visited = list()

        while current:
            try:
                next_obj = self.process.ptr(current + Global.NextObj)
                yield current
                if next_obj in visited:
                    break
                current = next_obj
            except:
                break

    def update(self):
        self.process.invalidate_cache()
        self._objects = dict()

        for offset in self._offsets():
            obj_type = self.process.byte(offset + ObjectOffsets.ObjType)
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
        target_guid = self.player().target()
        return self._objects[target_guid] if target_guid in self._objects else None
