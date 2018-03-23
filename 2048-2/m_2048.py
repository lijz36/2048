

import random
import os
import sys


mapL = []
Score = 0


def startRun():
    """初始化游戏列表数据"""
    global mapL
    for i in range(16):
        mapL.append(0)
    l = random.sample(range(16), 2)
    mapL[l[0]] = _ran_one_num(0, 16)
    mapL[l[1]] = _ran_one_num(0, 16)
    _print_map()


def _ran_one_num(start, stop):
    """随机生产２或４一个数"""
    r = random.randrange(start, stop)
    return 2 if r >= 2 else 4


def _print_map():
    """打印游戏图形界面"""
    os.system('clear')

    global mapL
    print("*********欢迎进入2048游戏平台*********")
    print("\t+" + "-" * 19 + "+")
    print("\t|", end='')
    for x in range(len(mapL)):
        if x != 0 and x % 4 == 0:
            print("\n\t+" + "-" * 19 + "+")
            print("\t|", end='')
        strs = str(mapL[x]).center(4) if mapL[x] > 0 else ' ' * 4
        print(strs + "|", end='')
    print("\n\t+" + "-" * 19 + "+")
    if _checkIsSuccess():
        endGame("您已成功完成2048任务")
    elif _checkIsOver():
         endGame("您未完成2048任务")


def _refresh_mapL():
    """刷新map和是否插入并打印"""
    if _check_is_insert():
        _ran_one_insert()
    else:
        _print_map()


def _check_is_insert():
    """检查是否可随机插入２或４"""
    global mapL
    for x in mapL:
        if x == 0:
            return True
    return False


def _checkIsSuccess():
    """判断是否胜利"""
    global mapL
    for i in mapL:
        if i == 2048:
            return True
    return False


def _checkIsOver():
    """检查游戏是否无法移动"""
    global mapL
    for j in range(0, len(mapL), 4):
        for i in range(j, j+3):
            if mapL[i] == mapL[i + 1]:
                return False
    for j in range(4):
        for i in range(j, len(mapL) - 4, 4):
            if mapL[i] == mapL[i + 4]:
                return False
    return True


def _ran_one_insert():
    """插入一个随机数"""
    global mapL
    lst = []
    for i in range(len(mapL)):
        if mapL[i] == 0:
            lst.append(i)
    j = random.choice(lst)
    mapL[j] = _ran_one_num(0, 16)
    _print_map()


def _left_a_line():
    """左移一步"""
    global mapL, Score
    for j in range(0, len(mapL), 4):
        # 此处注意索引加１超出的问题，所以为３
        for i in range(j, j + 3):
            if mapL[i] == 0:
                mapL[i] = mapL[i + 1]
                mapL[i + 1] = 0
            elif mapL[i] == mapL[i + 1]:
                mapL[i] *= 2
                mapL[i + 1] = 0
                Score += 1


def _right_a_line():
    """右移一步"""
    global mapL, Score
    for j in range(0, len(mapL), 4):
        for i in range(j + 3, j, -1):
            if mapL[i] == 0:
                mapL[i] = mapL[i - 1]
                mapL[i - 1] = 0
            elif mapL[i] == mapL[i - 1]:
                mapL[i] *= 2
                mapL[i - 1] = 0
                Score += 1


def _up_a_column():
    """上移一列"""
    global mapL, Score
    for j in range(4):
        for i in range(j, len(mapL) - 4, 4):
            if mapL[i] == 0:
                mapL[i] = mapL[i + 4]
                mapL[i + 4] = 0
            elif mapL[i] == mapL[i + 4]:
                mapL[i] *= 2
                mapL[i + 4] = 0
                Score += 1


def _down_a_column():
    """下移一列"""
    global mapL, Score
    for j in range(12, len(mapL)):
        for i in range(j, 4, -4):
            if mapL[i] == 0:
                mapL[i] = mapL[i - 4]
                mapL[i - 4] = 0
            elif mapL[i] == mapL[i - 4]:
                mapL[i] *= 2
                mapL[i - 4] = 0
                Score += 1


def leftMove():
    """左移"""
    for _ in range(3):
        _left_a_line()
    _refresh_mapL()


def rightMove():
    """右移"""
    for _ in range(3):
        _right_a_line()
    _refresh_mapL()


def updateMove():
    """上移"""
    for _ in range(3):
        _up_a_column()
    _refresh_mapL()


def downMove():
    """下移"""
    for _ in range(3):
        _down_a_column()
    _refresh_mapL()


def endGame(msg):
    """游戏结束"""
    print("**********2048游戏结束**********")
    print("结束原因：", msg)
    print("当前成绩：", Score)
    sys.exit(1)
