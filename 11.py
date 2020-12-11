#!/usr/bin/env python3

import fileinput
import itertools

rows = [[y for y in x.strip()] for x in fileinput.input()]

# Correct answers:
# p1: 2303
# p2: 2057

# Since the input is modified I cannot solve both P1 and P2 in the same go, I
# could keep a copy but haven't done it.
P2 = False  # Set True to solve P2


def occupied(m):
    diff = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    res = [None] * len(m)
    for (row, rv) in enumerate(m):
        res[row] = [0] * len(rv)
        for (col, cv) in enumerate(rv):
            if cv == ".":
                continue

            for (dr, dc) in diff:
                max_ = 1
                r = row
                c = col

                while True and max_ > 0:  # Break when non '.' found or out of bounds
                    if not P2:
                        max_ = 0

                    r += dr
                    c += dc
                    if r < 0 or r >= len(m):
                        break
                    elif c < 0 or c >= len(m[0]):
                        break

                    if m[r][c] == "#":
                        res[row][col] += 1
                        break
                    elif m[r][c] == "L":
                        break

    return res


def step(m):
    global P2

    occ = occupied(m)
    req = 5 if P2 else 4
    for (row, rv) in enumerate(m):
        for (col, cv) in enumerate(rv):
            if cv == "L" and occ[row][col] == 0:
                m[row][col] = "#"
            elif cv == "#" and occ[row][col] >= req:
                m[row][col] = "L"

    return occ  # m modified in place


prev_occ = step(rows)

while True:
    occ = step(rows)
    if prev_occ == occ:
        break
    prev_occ = occ


res = 0
for row in rows:
    res += row.count("#")

print("p2:" if P2 else "p1:", res)
