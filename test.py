from memory.process import Process
from memory.object_manager import ObjectManager
from control.autogui_controller import Controller
from reporting.bot import Bot
from algos.locator import Locator
from machines.rotation import Rotation
from algos.relativity import Relativity
from constants.offsets import Offsets
from constants.manual_offsets import Global, Camera
from constants.descriptors import CGUnitData, CGObjectData
import pyautogui

from machines.mob_farmer import MobFarmer

from components.mob_picker import MobPicker
from combat.priest import Model as PriestModel

from memory.camera import world_to_screen
from ui.window import Window

import logging
import time
import math
import importlib

import _recast as dt


def make_dump(player, count=50000, offset=4, func='int', desc=True):
    logging.info("waiting")

    for i in range(0, 5):
        time.sleep(1)
        logging.info(i)

    logging.info("snapshot")

    start_offset = player.descriptors if desc else player.offset

    values = list()
    for i in range(0, count):
        values.append(getattr(process, func)(start_offset + i * offset))

    time.sleep(5)
    logging.info("comparing")

    values2 = list()
    for i in range(0, count):
        values2.append(getattr(process, func)(start_offset + i * offset))

    for i in range(0, count):
        if values[i] != values2[i]:
            logging.info(f"diff for {i}: {values[i]} != {values2[i]}")


SIZE_OF_GRIDS = 533.33333

if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s](%(filename)-20s) [%(levelname)-5s]: %(message)s', level=logging.INFO)

    mmanager = dt.MMapManager("f:\\tmp\\wow_3.3.5\\")

    x = 1555.043212890625
    y = -4421.5478515625
    z = 8.577301979064941

    gx = int(32 - x / SIZE_OF_GRIDS)
    gy = int(32 - y / SIZE_OF_GRIDS)

    res = mmanager.load(1, gx, gy)

    nav_mesh = mmanager.mesh(1)

    filter = dt.dtQueryFilter()
    query = dt.dtNavMeshQuery()

    print("Init NavMesh Object")
    status = query.init(nav_mesh, 2048)
    if dt.dtStatusFailed(status):
        raise Exception("Fail")

    print("Fix The Input Data")
    polyPickExt = dt.dtVec3(7.0, 7.0, 7.0)

    process = Process("Wow.exe")
    manager = ObjectManager(process)
    window = Window()

    manager.update()
    startPos = dt.dtVec3(manager.player().y(), manager.player().z(), manager.player().x())
    status, out = query.findNearestPoly(startPos, polyPickExt, filter)

    startRef = out["nearestRef"]
    _startPt = out["nearestPt"]

    while True:
        manager.update()

        gx = int(32 - manager.player().x() / SIZE_OF_GRIDS)
        gy = int(32 - manager.player().y() / SIZE_OF_GRIDS)

        mmanager.load(1, gx, gy)

        logging.info(f"x: {manager.player().x()}, y: {manager.player().y()}, {manager.player().z()}")

        currentPos = dt.dtVec3(manager.player().y(), manager.player().z(), manager.player().x())
        status, out = query.findNearestPoly(currentPos, polyPickExt, filter)
        if dt.dtStatusFailed(status):
            logging.info("Failed to find")

        endRef = out["nearestRef"]
        _endPt = out["nearestPt"]

        status, out = query.findPath(startRef, endRef, startPos, currentPos, filter, 32)
        if dt.dtStatusFailed(status):
            break
        pathRefs = out["path"]

        status, fixEndPos = query.closestPointOnPoly(pathRefs[-1], currentPos)
        if dt.dtStatusFailed(status):
            break

        status, out = query.findStraightPath(startPos, fixEndPos, pathRefs, 32, 0)
        if dt.dtStatusFailed(status):
            break

        logging.info(f'{out["straightPath"]}, {out["straightPathFlags"]}, {out["straightPathRefs"]}')

        time.sleep(0.3)

    for o in manager.objects():
        logging.info(o)

    # while True:
    #     manager.update()
    #     logging.info(manager.player())
    #     target = manager.target()
    #     if target:
    #         logging.info(target)
    #         #make_dump(target)
    #         #break
    #     time.sleep(0.3)

        # for o in manager.objects():
        #     if o.target():
        #         logging.info(o)
        #
        #     logging.info(target.skin())
        #     time.sleep(0.3)
        #     make_dump(target)

    # name = manager.player_name.lower()
    name = 'Clrn'.lower()
    module = importlib.import_module(f'players.{name}')
    settings = getattr(module, 'PlayerSettings')()
    combat_model = settings.model(settings, manager)
    locator = Locator()
    picker = MobPicker(manager, locator, manager.player().position())
    with Bot() as telegram:
        with Controller(window) as controller:
            farmer = MobFarmer(window=window,
                               controller=controller,
                               object_manager=manager,
                               combat_model=combat_model,
                               mob_picker=picker,
                               telegram_bot=telegram)

            while True:
                try:
                    manager.update()
                    picker.update()
                    farmer.process()
                    locator.track(manager.player().x(), manager.player().y())
                except:
                    logging.exception("Main loop failed")
                    raise





