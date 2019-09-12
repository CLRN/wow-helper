from memory.process import Process
from constants.offsets import Offsets, Location
from constants.desriptors import CGUnitData
from memory.object_manager import ObjectManager
from algos.relativity import Relativity
from control.autogui_controller import Controller
from machines.rotation import Rotation
from machines.combat_action import CombatAction
from components.spell import Spell

import logging
import time
import math


def make_dump(player):
    logging.info("waiting")

    for i in range(0, 5):
        time.sleep(1)
        logging.info(i)

    logging.info("snapshot")

    values = list()
    for i in range(0, count):
        values.append(process.int(player.offset + i * 4))

    time.sleep(5)
    logging.info("comparing")

    values2 = list()
    for i in range(0, count):
        values2.append(process.int(player.offset + i * 4))

    for i in range(0, count):
        if values[i] and not values2[i]:
            logging.info(f"diff for {i}: {values[i]}")


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    process = Process("Wow.exe")
    manager = ObjectManager(process)

    count = 2000

    manager.update()
    player = manager.player()

    # make_dump(player)

    controller = Controller()
    rotation = Rotation(controller)
    action = CombatAction(controller)

    smite_spell = Spell(2, 25, 2, '2', 0)

    while True:
        manager.update()
        t = manager.target()
        if t:
            rotation.process(math.degrees(Relativity.angle(player, t)))
            action.process(Relativity.distance(player, t), smite_spell, player.spell())
        else:
            logging.info('No target')
            time.sleep(1)

    while True:
        logging.info(manager.objects())
        logging.info(manager.player())

        target = manager.target()
        if target:
            logging.info(target)
            tot = target.target()
            if tot:
                logging.info(manager.object(tot))

        time.sleep(1)





