#!/usr/bin/env python3

import fileinput
import re

r = re.compile("\(\[\w ]+\)bags?\( \d+ \([\w ]+\) bags?,?\)*")

lines = [x.strip() for x in fileinput.input()]

can_hold = set()
info = {}

p1 = 0
p2 = 0
for line in lines:
    beg, end = line.split("contain")
    bag = beg.split("bags")[0].strip()

    if "no other bags" in end:
        continue

    holds = []
    for rem in end.split(","):

        parts = rem.strip().split(" ")
        num = int(parts[0])
        col = " ".join(parts[1:-1])
        # holds.append((num, col))
        holds.append(col)

    info[bag] = holds

queue = []
visited = []
res = set()

# Recursive find bag's which can hold the specified bag
def can_hold(bag):
    for b in info:
        if bag in info[b] and not info[b] in queue and not info[b] in visited:
            queue.append(b)
            res.add(b)
        # print(queue)

        # print(f"{bag} can be in {b}")


# start queue
can_hold("shiny gold")
while len(queue) > 0:
    bag = queue.pop(0)
    visited.append(bag)

    can_hold(bag)


# print(res)
# print(can_hold("shiny gold"))


# print(info)
print("p1:", len(res))
print("p2:", p2)
