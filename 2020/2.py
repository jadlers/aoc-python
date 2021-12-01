#!/usr/bin/env python3

import fileinput
import re

# Example line:
# 6-12 p: pfpppzpppzpbpg


p1 = 0
p2 = 0
p = re.compile("(\d+)-(\d+) ([a-z]): (\w+)")
xs = [x for x in fileinput.input()]

for x in xs:
    res = p.match(x)
    start = int(res.group(1))
    end = int(res.group(2))
    letter = res.group(3)
    pw = res.group(4)

    searched = [x for x in pw if x == letter]

    if start <= len(searched) <= end:
        p1 += 1

    if (pw[start - 1] == letter) ^ (pw[end - 1] == letter):
        p2 += 1


print("part1: ", p1)
print("part1: ", p2)
