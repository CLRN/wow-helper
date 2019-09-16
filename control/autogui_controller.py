from components.settings import Settings
import pyautogui
from pyautogui.tweens import easeInOutElastic, easeInOutCubic, easeInOutExpo
import random
import time
import logging
from threading import Thread, Lock
import os
import shutil


class Controller(Thread):
    def __init__(self, window):
        if os.path.exists('screens'):
            shutil.rmtree('screens')
        os.makedirs('screens')

        self.window = window

        self.queue = list()
        self.is_running = True
        self.lock = Lock()

        Thread.__init__(self, target=self._thread_func)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_running = False
        self.join()

    def _thread_func(self):
        while self.is_running:
            with self.lock as _:
                item_to_do = self.queue[0] if len(self.queue) else None
                if item_to_do:
                    self.queue.pop(0)

            if item_to_do:
                try:
                    func, args = item_to_do
                    func(*args)
                except:
                    logging.exception(f"Exception in controller thread")

            time.sleep(self.random_pause())

    @staticmethod
    def random_pause():
        return random.randint(100, 300) / 1000

    def up(self, key):
        pyautogui.keyUp(key)

    def down(self, key):
        pyautogui.keyDown(key)

    def _press(self, button):
        if isinstance(button, tuple):
            hot_key, key = button

            pyautogui.keyDown(hot_key, pause=self.random_pause())
            pyautogui.press(key, pause=self.random_pause())
            pyautogui.keyUp(hot_key)
        else:
            pyautogui.press(button, pause=self.random_pause())

    def _click(self, x, y):
        tween = random.choice([easeInOutElastic, easeInOutCubic, easeInOutExpo])
        pyautogui.rightClick(x, y, tween=tween, duration=random.randint(200, 500) / 1000)

    def _screen(self):
        rect = self.window.rect()
        screen = pyautogui.screenshot(region=(rect.left_top[0], rect.left_top[1], rect.bottom_right[0], rect.bottom_right[1]))
        screen.save(f'./screens/{int(time.time())}.png')

    def _enqueue(self, func, args):
        assert self.is_running

        to_pop = None
        with self.lock as _:
            for i in range(len(self.queue)):
                if self.queue[i][0] == func:
                    to_pop = i
                    break

            if to_pop is not None:
                self.queue.pop(to_pop)

            self.queue.append((func, args))

    def press(self, button):
        self._enqueue(self._press, button)

    def click(self, x, y):
        self._enqueue(self._click, (x, y))

    def screen(self):
        self._enqueue(self._screen, ())
