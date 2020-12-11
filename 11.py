#!/usr/bin/env python3

import fileinput
import itertools

rows = [[y for y in x.strip()] for x in fileinput.input()]


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
            # print(f"Now at {r, c}")
            for (dr, dc) in diff:
                # print(f"row={row} col={col} dr={dr} dc={dc}", end=" ")
                r = row + dr
                c = col + dc
                if r < 0 or r >= len(m):
                    # print()
                    continue
                if c < 0 or c >= len(m[0]):
                    # print()
                    continue

                # print(f"m[{r}][{c}] = {m[r][c]}")
                if m[r][c] == "#":
                    res[row][col] += 1

    # print(f"r={r} c={c}")
    # for row in res:
    #     print(row)
    return res


def step(m):
    occ = occupied(m)
    for (row, rv) in enumerate(m):
        for (col, cv) in enumerate(rv):
            # print(occ[row][col])
            if cv == "L" and occ[row][col] == 0:
                m[row][col] = "#"
            elif cv == "#" and occ[row][col] >= 4:
                m[row][col] = "L"

    return occ  # m modified in place


p1 = 0
p2 = 0

# print(occupied(rows, 0, 0))

prev_occ = step(rows)
while True:
    occ = step(rows)
    if prev_occ == occ:
        break
    prev_occ = occ


for row in rows:
    p1 += row.count("#")
# prev_occ = step(rows)
# for row in rows:
#     print(row)
# for col in row:
#     break
# print(adjacent(row, col))

print("p1:", p1)
print("p2:", p2)
