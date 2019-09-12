import pyautogui
import random


class Controller:
    @staticmethod
    def random_pause():
        return random.randint(100, 300) / 1000

    def up(self, key):
        pyautogui.keyUp(key, pause=self.random_pause())

    def down(self, key):
        pyautogui.keyDown(key, pause=self.random_pause())

    def press(self, button):
        pyautogui.press(button, pause=self.random_pause())
