#!/usr/bin/env python3

import fileinput

line = [x for x in fileinput.input()]
time = int(line[0])
ids = [int(x) if x != "x" else -1 for x in line[1].split(",")]
print(ids)

MAX = time + max(ids)
print(MAX)


# Part 1
shuttle_times = []
for id_ in ids:
    if id_ == -1:  # Skip (x input)
        continue

    t = id_
    while t < time:
        t += id_

    shuttle_times.append((t, id_))

departure, bus_id = min(shuttle_times)
p1 = (departure - time) * bus_id
print("p1:", p1)


p2 = 0

print("p2:", p2)
