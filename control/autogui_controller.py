from components.settings import Settings
import pyautogui
from pyautogui.tweens import easeInOutElastic, easeInOutCubic, easeInOutExpo
import random
import time
import logging


class Controller:
    def __init__(self):
        self.last_action = time.time()

    def _check_and_update_last_action(self):
        spent = time.time() - self.last_action
        if spent < Settings.MIN_ACTION_DELAY_SECONDS:
            return False
        else:
            self.last_action = time.time()
            return True

    @staticmethod
    def random_pause():
        return random.randint(100, 300) / 1000

    def up(self, key):
        pyautogui.keyUp(key)

    def down(self, key):
        pyautogui.keyDown(key)

    def press(self, button):
        if self._check_and_update_last_action():
            if isinstance(button, tuple):
                hot_key, key = button

                pyautogui.keyDown(hot_key, pause=self.random_pause())
                pyautogui.press(key, pause=self.random_pause())
                pyautogui.keyUp(hot_key)
            else:
                pyautogui.press(button, pause=self.random_pause())

    def click(self, x, y):
        if self._check_and_update_last_action():
            tween = random.choice([easeInOutElastic, easeInOutCubic, easeInOutExpo])
            pyautogui.rightClick(x, y, tween=tween, duration=random.randint(200, 500) / 1000)
