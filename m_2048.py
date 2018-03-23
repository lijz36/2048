

import random
import time


mapL = []
Score = 0


def F_Run():
    """开始游戏"""
    global mapL
    mapL = [[0 for x in range(4)] for y in range(4)]
    for x in range(2):
        l = ran_one_list_index()
        mapL[l[0]][l[1]] = ran_one_num(0, 16)
    print_mapL()


# 随机生产２或４一个数
def ran_one_num(s, e):
    r = random.randrange(s, e)
    return 2 if r >= 2 else 4


def ran_one_list_index():
    """随机生成一个数的索引列表"""
    lst = []
    temp = []

    def _is_have_zone(i):
        for x in mapL[i]:
            if x == 0:
                return True
        return False

    while True:
        r1 = random.randrange(0, 4)
        if r1 not in temp:
            if _is_have_zone(r1):
                r2 = random.randrange(0, 4)
                if mapL[r1][r2] == 0:
                    lst += [r1, r2]
                    break
            else:
                temp.append(r1)
    return lst


def print_mapL():
    """打印游戏图形界面"""
    global mapL
    print("+" + "-" * 19 + "+")
    count = 0
    for x in mapL:
        count += 1
        print("|", end='')
        for y in x:
            strs = str(y).center(4) if y > 0 else ' ' * 4
            print(strs + "|", end='')
        if count < 4:
            print("\n+" + "-" * 19 + "+")
        else:
            print()
    print("+" + "-" * 19 + "+")


def _left_a_line():
    """左移一步"""
    global mapL, Score
    for l in mapL:
        for i in range(3):
            if l[i] == 0:
                l[i] = l[i + 1]
                l[i + 1] = 0
            else:
                if l[i] == l[i + 1]:
                    l[i] *= 2
                    l[i + 1] = 0
                    Score += 1


def _right_a_line():
    """右移一步"""
    global mapL, Score
    for l in mapL:
        for i in range(-1, -4, -1):
            if l[i] == 0:
                l[i] = l[i - 1]
                l[i - 1] = 0
            else:
                if l[i] == l[i - 1]:
                    l[i] *= 2
                    l[i - 1] = 0
                    Score += 1


def _up_a_column():
    """上移一列"""
    global mapL, Score
    for i in range(4):
        for j in range(3):
            if mapL[j][i] == 0:
                mapL[j][i] = mapL[j + 1][i]
                mapL[j + 1][i] = 0
            else:
                if mapL[j][i] == mapL[j + 1][i]:
                    mapL[j][i] *= 2
                    mapL[j + 1][i] = 0
                    Score += 1


def _down_a_column():
    """下移一列"""
    global mapL, Score
    for i in range(4):
        for j in range(3, 0, -1):
            if mapL[j][i] == 0:
                mapL[j][i] = mapL[j - 1][i]
                mapL[j - 1][i] = 0
            else:
                if mapL[j][i] == mapL[j - 1][i]:
                    mapL[j][i] *= 2
                    mapL[j - 1][i] = 0
                    Score += 1


def _check_is_insert():
    """是否可插入"""
    global mapL
    for l in mapL:
        for x in l:
            if x == 0:
                return True
    return False


def _ran_one_insert():
    """插入一个随机数"""
    global mapL
    l = ran_one_list_index()
    mapL[l[0]][l[1]] = ran_one_num(0, 16)
    print_mapL()


def _refresh_mapL():
    """刷新map和是否插入并打印"""
    if _check_is_insert():
        _ran_one_insert()
    else:
        print_mapL()


def F_GameOver(msg):
    """游戏结束"""
    print("**********2048游戏结束**********")
    print("结束原因：", msg)
    print("当前成绩：", Score)


def F_LeftMove():
    """左移"""
    for _ in range(3):
        _left_a_line()
    _refresh_mapL()


def F_RightMove():
    """右移"""
    for _ in range(3):
        _right_a_line()
    _refresh_mapL()


def F_UpMove():
    """上移"""
    for _ in range(3):
        _up_a_column()
    _refresh_mapL()


def F_DownMove():
    """下移"""
    for _ in range(3):
        _down_a_column()
    _refresh_mapL()
