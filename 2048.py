
"""2048主程序"""

import m_2048 as T
import sys
import os


def show_input():
    while True:
        action = input("Move:")
        if action == 'A' or action == "a":
            os.system('clear')
            print("左移<<<")
            T.F_LeftMove()
        elif action == 'D' or action == "d":
            os.system('clear')
            print("右移>>>")
            T.F_RightMove()
        elif action == 'W' or action == "w":
            os.system('clear')
            print("上移↑↑↑")
            T.F_UpMove()
        elif action == 'S' or action == "s":
            os.system('clear')
            print("右移↓↓↓")
            T.F_DownMove()
        elif action == 'Q' or action == "q":
            os.system('clear')
            T.F_GameOver("人为结束")
            break
        else:
            continue


if __name__ == "__main__":
    print("**********欢迎进入2048游戏平台**********")

    T.F_Run()

    show_input()

sys.exit()
