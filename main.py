import os.path
import time
import keyboard
import json
import playsound3
from win32api import mouse_event, keybd_event
from win32con import KEYEVENTF_KEYUP
# pyinstaller -F -i icon.ico main.py
key_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z",
            "BACKSPACE", "TAB", 
            "SHIFT", "CTRL", "ALT",
            "RIGHT SHIFT", "RIGHT CTRL", "RIGHT ALT",
            "PAUSE", "BREAK", "CAPS LOCK", "ESC",
            "SPACE", "PAGE UP", "PAGE DOWN", "END", "HOME",
            "LEFT", "UP", "RIGHT", "DOWN", "PRINT SCREEN", 
            "INSERT", "DELETE", 
            "LEFT WINDOWS", "RIGHT WINDOWS", 
            "NUM LOCK", "decimal", "\\", ".", ";", "\"", ","
            "[", "]", "+", "-", "~", "`", "/"]
press_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
              "F9", "F10", "F11", "F12", "F13", "F14", "F15", "F16",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z",
              "BACKSPACE", "TAB", "TABLE", "CLEAR",
              "ENTER", "SHIFT", "CTRL",
              "CONTROL", "ALT", "ALTER", "PAUSE", "BREAK", "CAPSLK", "CAPSLOCK", "ESC",
              "SPACE", "SPACEBAR", "PGUP", "PAGEUP", "PGDN", "PAGEDOWN", "END", "HOME",
              "LEFT", "UP", "RIGHT", "DOWN", "SELECT", "PRTSC", "PRINTSCREEN", "SYSRQ",
              "SYSTEMREQUEST", "EXECUTE", "SNAPSHOT", "INSERT", "DELETE", "HELP", "WIN",
              "WINDOWS", "NMLK", "VOLUMEMUTE",
              "NUMLK", "NUMLOCK", "SCRLK",
              "[", "]", "+", "-", "~", "`", "/"]
mouse_list = ["LCLICK", "RCLICK", "MCLICK"]
press_map = {
        "0": 48, "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55, "8": 56, "9": 57,
        "F1": 112, "F2": 113, "F3": 114, "F4": 115, "F5": 116, "F6": 117, "F7": 118, "F8": 119,
        "F9": 120, "F10": 121, "F11": 122, "F12": 123, "F13": 124, "F14": 125, "F15": 126, "F16": 127,
        "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
        "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
        "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90,
        "BACKSPACE": 8, "TAB": 9, "TABLE": 9, "CLEAR": 12,
        "ENTER": 13, "SHIFT": 16, "CTRL": 17,
        "CONTROL": 17, "ALT": 18, "ALTER": 18, "PAUSE": 19, "BREAK": 19, "CAPSLK": 20, "CAPSLOCK": 20, "ESC": 27,
        "SPACE": 32, "SPACEBAR": 32, "PGUP": 33, "PAGEUP": 33, "PGDN": 34, "PAGEDOWN": 34, "END": 35, "HOME": 36,
        "LEFT": 37, "UP": 38, "RIGHT": 39, "DOWN": 40, "SELECT": 41, "PRTSC": 42, "PRINTSCREEN": 42, "SYSRQ": 42,
        "SYSTEMREQUEST": 42, "EXECUTE": 43, "SNAPSHOT": 44, "INSERT": 45, "DELETE": 46, "HELP": 47, "WIN": 91,
        "WINDOWS": 91, "NMLK": 144, "VOLUMEMUTE": 173,
        "NUMLK": 144, "NUMLOCK": 144, "SCRLK": 145,
        "[": 219, "]": 221, "+": 107, "-": 109, "~": 192, "`": 192, "/": 111}


def lclick():
    mouse_event(2, 0, 0)
    time.sleep(0.01)
    mouse_event(4, 0, 0)
    time.sleep(0.01)


def rclick():
    mouse_event(8, 0, 0)
    time.sleep(0.01)
    mouse_event(16, 0, 0)
    time.sleep(0.01)


def mclick():
    mouse_event(32, 0, 0)
    time.sleep(0.01)
    mouse_event(64, 0, 0)
    time.sleep(0.01)


def press(key):
    key_num = press_map[key.upper()]
    keybd_event(key_num, 0, 0, 0)
    keybd_event(key_num, 0, KEYEVENTF_KEYUP, 0)


def pt_set(_dir):
    while 1:
        disable = _dir["disable"]
        key = _dir["key"]
        pres = _dir["press"]
        interval = _dir["interval"]
        print("---PressTrigger---\n"
              "本工具作者B站up：绘星痕\n"
              "项目地址：\n"
              "----------------------------------------------------\n"
              "当前设置：\n"
              f"   禁用热键：  {disable}\n"
              f"   触发键：    {key}\n"
              f"   连击键：    {pres}\n"
              f"   连击间隔：  {interval}\n"
              "按下\"Enter\"开始，或输入对应数字进行设置。\n"
              "   0.依次设置\n"
              "   1.开关热键\n"
              "   2.触发键\n"
              "   3.连击键\n"
              "   4.点击间隔（单位：秒）"
              )
        choose = input("按下\"Enter\"可开始：")
        if choose in ["0", "1", "2", "3", "4"]:
            if choose in ["0", "1"]:
                _disable = input("输入热键用以禁用连点:").upper()
                if _disable == "":
                    pass
                elif _disable in _dir["key_list"]:
                    _dir["disable"] = _disable
                else:
                    print("无效指令")
                    pass
            if choose in ["0", "2"]:
                _key = input("输入启动单键(键盘或者鼠标):").upper()
                if _key == "":
                    pass
                elif _key in _dir["key_list"]:
                    _dir["key"] = _key
                elif _key == ", ":
                    _dir["key"] = ""
                else:
                    print("无效指令")
                    pass
            if choose in ["0", "3"]:
                _key = input("输入连击单键(键盘或者鼠标):").upper()
                if _key == "":
                    pass
                elif _key in _dir["press_list"]+_dir["mouse_list"]:
                    _dir["press"] = _key
                else:
                    print("无效指令")
                    pass
            if choose in ["0", "4"]:
                _interval = float(input("输入点击间隔（单位：秒）:"))
                _dir["interval"] = _interval
            with open("config.json", "w", encoding="utf-8") as file:
                json.dump(_dir, file)
        elif choose:
            print("无效指令")
            continue
        else:
            break


def clicker(_dir):
    disable, key, pre, inter = _dir["disable"].upper(), _dir["key"].upper(), _dir["press"].upper(), _dir["interval"]
    print(f"长按 '{key}' 触发连击, 短按 '{disable}' 禁用触发")
    while 1:
        while 1:
            _name = keyboard.read_event().name.upper()
            if _name == disable:
                break
            elif _name == key:
                print("连点器启动")
                if pre.upper() in _dir["mouse_list"]:
                    if pre.upper() == "LCLICK":
                        while keyboard.is_pressed(key):
                            lclick()
                            time.sleep(inter)
                    elif pre.upper() == "RCLICK":
                        while keyboard.is_pressed(key):
                            rclick()
                            time.sleep(inter)
                    elif pre.upper() == "MCLICK":
                        while keyboard.is_pressed(key):
                            mclick()
                            time.sleep(inter)
                else:
                    while keyboard.is_pressed(key):
                        press(pre)
                        time.sleep(inter)
                print("连点器停止")
        playsound3.playsound("switch.mp3")
        print(f"触发已禁用, 短按 '{disable}' 启用触发")
        keyboard.wait(disable)
        playsound3.playsound("switch.mp3")
        print(f"触发已启用, 短按 '{disable}' 禁用触发")
        time.sleep(0.5)


def main():
    _dir = {
            "disable": "`",
            "key": "s",
            "press": "rclick",
            "interval": 0,
            "key_list": key_list,
            "press_list": press_list,
            "mouse_list": mouse_list}
    if os.path.exists("config.json"):
        with open("config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
        if config:
            _dir.update(config)
    pt_set(_dir)
    clicker(_dir)


if __name__ == "__main__":
    main()
