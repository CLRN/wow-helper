from memory.process import Process
from memory.object_manager import ObjectManager
from algos.relativity import Relativity
from control.autogui_controller import Controller
from machines.rotation import Rotation
from machines.combat_action import CombatAction
from machines.mob_search import MobSearch
from components.spell import Spell
from components.mob_picker import MobPicker

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
    logging.basicConfig(format='[%(asctime)s](%(filename)-20s) [%(levelname)-5s]: %(message)s', level=logging.DEBUG)

    process = Process("Wow.exe")
    manager = ObjectManager(process)

    count = 2000

    manager.update()
    player = manager.player()

    # make_dump(player)

    controller = Controller()
    rotation = Rotation(controller)
    action = CombatAction(controller)
    search = MobSearch(controller)

    smite_spell = Spell(2, 25, 2, '2', 0)

    mob = MobPicker(manager).pick()

    logging.info(f"Going to {mob}")

    while True:
        manager.update()
        rotation.process(math.degrees(Relativity.angle(player, mob)))

        target = manager.target()
        if target:
            logging.info(f"Mob: {mob}, Target {manager.target()}")

        search.process(Relativity.distance(player, mob), target.id() == mob.id() if target else False)
        if search.is_selected:
            break

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





