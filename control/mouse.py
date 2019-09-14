import pyautogui
import time


class Mouse:
    def hover(self, x, y):
        pyautogui.moveTo(x, y, duration=0.1)
