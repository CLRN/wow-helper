from control.autogui_controller import Controller
import pyautogui
import random


class KeyboardController(Controller):
    def loot(self):
        pyautogui.press('4', pause=self.random_pause())
        pyautogui.press('-', pause=self.random_pause())

    def tab(self):
        pyautogui.press('tab', pause=random.randint(30, 80) / 100)
