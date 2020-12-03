#!/usr/bin/env python3

import fileinput

lines = [x.strip() for x in fileinput.input()]


def slope_trees(dx, dy):
    trees = 0
    x = 0
    y = 0

    while y < len(lines):
        xc = x % len(lines[0])
        if lines[y][xc] == "#":
            trees += 1

        x += dx
        y += dy

    return trees


p1 = slope_trees(3, 1)
print("p1:", p1)

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

p2 = 1
for [dx, dy] in slopes:
    p2 *= slope_trees(dx, dy)

print("p2:", p2)
