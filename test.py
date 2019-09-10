from process import Process
from offsets import Offsets, Location, Descritor

import logging
import time


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    p = Process("Wow.exe")
    local_player_id = p.int(p.base_address + Offsets.LocalPlayerGUID)
    logging.info(f"Starting: {p.str(p.base_address + Offsets.Version, 10)}.{p.str(p.base_address + Offsets.Build, 10)},"
                 f" date: {p.str(p.base_address + Offsets.Date, 20)}")
    logging.info(f"Player GUID: {local_player_id}")

    obj_manager = p.ptr(p.base_address + Offsets.ObjMgrPtr)
    current = p.ptr(obj_manager + Offsets.FirstObj)
    while current:
        player_id = p.int(current + Offsets.ObjGUID)

        if player_id == local_player_id:
            break
        current = p.ptr(current + Offsets.NextObj)

    descriptors = p.ptr(current + Offsets.Descriptors)
    while True:
        hp = p.int(descriptors + Descritor.HP * 4)
        mana = p.int(descriptors + Descritor.Mana * 4)

        logging.info(f"Object, id: {player_id}, "
                     f"type: {p.byte(current + Offsets.ObjType)}, "
                     f"HP: {hp}, "
                     f"Mana: {mana}, "
                     f"x: {p.float(current + Offsets.UnitPosition + Location.X)}, "
                     f"y: {p.float(current + Offsets.UnitPosition + Location.Y)}, "
                     f"z: {p.float(current + Offsets.UnitPosition + Location.Z)}, "
                     f"r: {p.float(current + Offsets.UnitPosition + Location.R)}, ")
        time.sleep(1)





