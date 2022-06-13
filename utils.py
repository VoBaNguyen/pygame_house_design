import math


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0


def distance(A, B):
    xA, yA = A
    xB, yB = B
    dis = math.sqrt((xB-xA)**2+(yB-yA)**2)
    return int(dis)


def mid(A, B):
    xA, yA = A
    xB, yB = B
    return [(xA+xB)/2, (yA+yB)/2]
