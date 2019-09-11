from process import Process
from offsets import Offsets, Location
from desriptors import CGUnitData

import logging
import time


def print_unit(current):
    descriptors = p.ptr(current + Offsets.Descriptors) + 4

    logging.info(f"Object, id: {p.ptr(current + Offsets.ObjGUID)}, "
                 f"type: {p.byte(current + Offsets.ObjType)}, "
                 f"HP: {p.int(descriptors + CGUnitData.health * 4)}, "
                 f"Mana: {p.int(descriptors + CGUnitData.power * 4)}, "
                 f"level: {p.int(descriptors + CGUnitData.level * 4)}, "
                 f"target: {p.ptr(descriptors + CGUnitData.target * 4)}, "
                 f"npcFlags: {p.ptr(descriptors + CGUnitData.npcFlags * 4)}, "
                 f"x: {p.float(current + Offsets.UnitPosition + Location.X)}, "
                 f"y: {p.float(current + Offsets.UnitPosition + Location.Y)}, "
                 f"z: {p.float(current + Offsets.UnitPosition + Location.Z)}, "
                 f"r: {p.float(current + Offsets.UnitPosition + Location.R)}, ")


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    p = Process("Wow.exe")

    local_player_id = p.ptr(p.base_address + Offsets.LocalPlayerGUID)
    logging.info(f"Starting: {p.str(p.base_address + Offsets.Version, 10)}.{p.str(p.base_address + Offsets.Build, 10)},"
                 f" date: {p.str(p.base_address + Offsets.Date, 20)}")

    target_guid = p.ptr(p.base_address + Offsets.TargetGuid)
    logging.info(f"Player GUID: {local_player_id}, target GUID: {target_guid}")

    obj_manager = p.ptr(p.base_address + Offsets.ObjMgrPtr)

    while True:
        current = p.ptr(obj_manager + Offsets.FirstObj)

        while current:
            unit_id = p.ptr(current + Offsets.ObjGUID)
            if unit_id == target_guid or unit_id == local_player_id:
                try:
                    print_unit(current)
                except:
                    break

                values = list()
                descriptors = p.ptr(current + Offsets.Descriptors) + 4
                for i in range(0, 300):
                    values.append((i, p.int(descriptors + i * 4)))

                # logging.info(values)

            current = p.ptr(current + Offsets.NextObj)

        time.sleep(1)




