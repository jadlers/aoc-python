import fileinput
import sys


lines = [(x[0], int(x[1:])) for x in fileinput.input()]

x = 0
y = 0
wx = 10
wy = 1
facing = 90


def rotate(deg, x, y):
    new_x, new_y = x, y
    if deg == 180:
        return -x, -y
    elif deg == 90:
        if x > 0 and y > 0:
            new_x = y
            new_y = -1 * x
        elif x > 0 and y < 0:
            new_x = y
            new_y = -1 * x
        elif x < 0 and y < 0:
            new_x = y
            new_y = -1 * x
        elif x < 0 and y > 0:
            new_x = y
            new_y = -1 * x

        x, y = new_x, new_y
    elif deg == 270:
        x, y = rotate(90, x, y)
        x, y = rotate(90, x, y)
        x, y = rotate(90, x, y)

    return x, y


def fdir(degree):
    if degree == 0:
        return "N"
    elif degree == 90:
        return "E"
    elif degree == 180:
        return "S"
    elif degree == 270:
        return "W"

    return None


def p1():
    global x, y, facing
    x, y = 0, 0

    for (d, l) in lines:
        if d == "N" or d == "F" and facing == 0:
            y += l
        elif d == "E" or d == "F" and facing == 90:
            x += l
        elif d == "S" or d == "F" and facing == 180:
            y -= l
        elif d == "W" or d == "F" and facing == 270:
            x -= l
        elif d == "R":
            facing += l
            facing %= 360
            assert facing in [0, 90, 180, 270]
        elif d == "L":
            facing -= l
            facing %= 360
            assert facing in [0, 90, 180, 270]
    return abs(x) + abs(y)


def p2():
    global x, y, wx, wy
    x, y = 0, 0
    wx, wy = 10, 1

    for (d, l) in lines:
        # Move waypoint
        if d == "N":
            wy += l
        elif d == "E":
            wx += l
        elif d == "S":
            wy -= l
        elif d == "W":
            wx -= l

        # Move ship
        elif d == "F":
            x += wx * l
            y += wy * l

        # Rotate waypoint
        elif d == "R":
            deg = l % 360
            wx, wy = rotate(deg, wx, wy)
        elif d == "L":
            deg = -l % 360
            wx, wy = rotate(deg, wx, wy)
        else:
            assert False
            print("GOT HERE")

    return abs(x) + abs(y)


# p1: 7136 not correct, 6864 not correct, CORRECT: 858
# p2: 244350 too high, 39134 too low
print("p1:", p1())
print("p2:", p2())
