

"""2048主程序"""
import sys
import m_2048 as T


def show_input():
    while True:
        action = input("Move:")
        if action == 'A' or action == "a":
            print("左移<<<")
            T.leftMove()
        elif action == 'D' or action == "d":
            print("右移>>>")
            T.rightMove()
        elif action == 'W' or action == "w":
            print("上移↑↑↑")
            T.updateMove()
        elif action == 'S' or action == "s":
            print("下移↓↓↓")
            T.downMove()
        elif action == 'Q' or action == "q":
            T.endGame("玩家主动退出游戏")
            break


if __name__ == "__main__":
    T.startRun()
    show_input()
