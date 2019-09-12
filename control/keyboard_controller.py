from control.autogui_controller import Controller
import pyautogui


class KeyboardController(Controller):
    def loot(self):
        pyautogui.press('4', pause=self.random_pause())
        pyautogui.press('-', pause=self.random_pause())
