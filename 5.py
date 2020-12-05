#!/usr/bin/env python3

import fileinput
import math


def higher(lo, hi):
    move = math.ceil((hi - lo) / 2)
    return lo + move


def lower(lo, hi):
    move = math.ceil((hi - lo) / 2)
    return hi - move


seats = []
lines = [x.strip() for x in fileinput.input()]
for line in lines:
    lo, hi = 0, 127
    for ch in range(7):
        if line[ch] == "B":
            lo = higher(lo, hi)
        else:
            hi = lower(lo, hi)
    row = lo if line[6] == "L" else hi

    lo, hi = 0, 7
    for ch in range(7, len(line)):
        if line[ch] == "R":
            lo = higher(lo, hi)
        else:
            hi = lower(lo, hi)

    col = lo
    seats.append((row * 8) + col)

p1 = max(seats)
print("p1:", p1)

seats.sort()
last = 0
for i in range(len(seats) - 1):
    if seats[i] + 1 != seats[i + 1]:
        p2 = seats[i] + 1

print("p2:", p2)
