from control.autogui_controller import Controller
import pyautogui
import random


class KeyboardController(Controller):
    def loot(self):
        pyautogui.press('4', pause=random.randint(500, 900) / 500)
        pyautogui.press('-', pause=random.randint(300, 800) / 500)

    def tab(self):
        pyautogui.press('tab', pause=random.randint(30, 80) / 100)
