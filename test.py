from memory.process import Process
from constants.offsets import Offsets, Location
from constants.desriptors import CGUnitData
from memory.object_manager import ObjectManager

import logging
import time

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    process = Process("Wow.exe")
    manager = ObjectManager(process)

    while True:
        manager.update()

        logging.info(manager.objects())
        logging.info(manager.player())

        target = manager.target()
        if target:
            logging.info(target)
            tot = target.target()
            if tot:
                logging.info(manager.object(tot))

        time.sleep(1)





