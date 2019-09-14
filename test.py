from memory.process import Process
from memory.object_manager import ObjectManager
from control.keyboard_controller import KeyboardController
from machines.rotation import Rotation
from algos.relativity import Relativity
from constants.offsets import Offsets
from constants.manual_offsets import Global, Camera
from control.mouse import Mouse

from machines.mob_farmer import MobFarmer

from components.mob_picker import MobPicker
from combat.priest import Model as PriestModel

from memory.camera import world_to_screen
from ui.window import Window

import logging
import time
import math


def make_dump(player, count=10000, offset=4, func='int', desc=True):
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
            logging.info(f"diff for {i}: {values[i]}")


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s](%(filename)-20s) [%(levelname)-5s]: %(message)s', level=logging.DEBUG)

    process = Process("Wow.exe")
    manager = ObjectManager(process)
    window = Window()
    mouse = Mouse()

    while True:
        manager.update()

        target = manager.target()
        if target:
            x, y = world_to_screen(process, window, target.x(), target.y(), target.z())
            logging.info((x, y))
            mouse.hover(x, y)

        time.sleep(0.3)

    controller = KeyboardController()
    model = PriestModel()
    picker = MobPicker(manager)

    farmer = MobFarmer(controller=controller,
                       object_manager=manager,
                       combat_model=model,
                       mob_picker=picker)

    rotation = Rotation(controller)
    # while True:
    #     manager.update()
    #     if manager.target():
    #         angle = Relativity.angle(manager.player(), manager.target())
    #         # time.sleep(0.5)
    #         rotation.process(angle)

    while True:
        manager.update()
        farmer.process()





