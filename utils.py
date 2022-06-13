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


def vector(A, B):
    xA, yA = A
    xB, yB = B
    return [xB-xA, yB-yA]


def mid(A, B):
    xA, yA = A
    xB, yB = B
    return [(xA+xB)/2, (yA+yB)/2]


def relative_pos(rect_move, rect_fixed):
    if rect_move.right <= rect_fixed.left:
        return "left"
    elif rect_move.left >= rect_fixed.right:
        return "right"
    elif rect_move.bottom >= rect_fixed.top:
        return "bottom"
    elif rect_move.top <= rect_fixed.bottom:
        return "top"
    else:
        return "Undetermined"
