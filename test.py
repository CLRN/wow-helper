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


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s](%(filename)-20s) [%(levelname)-5s]: %(message)s', level=logging.INFO)

    process = Process("Wow.exe")
    manager = ObjectManager(process)
    window = Window()

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





