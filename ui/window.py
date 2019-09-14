import win32gui


class Rect:
    def __init__(self, left_top, bottom_right):
        self.left_top = left_top
        self.bottom_right = bottom_right


class Window:
    def __init__(self):
        self.handle = win32gui.FindWindow('GxWindowClass', 'World Of Warcraft')
        assert self.handle

    def rect(self):
        rect = win32gui.GetWindowRect(self.handle)
        return Rect((rect[0], rect[1]), (rect[2], rect[3]))

    def client_to_screen(self, x, y):
        return win32gui.ClientToScreen(self.handle, (x, y))
