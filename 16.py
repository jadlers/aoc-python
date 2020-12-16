#!/usr/bin/env python3

import fileinput
import re

lines = [x.strip() for x in fileinput.input()]

block = 0

valid = {}
p1 = 0
for line in lines:
    if not line:
        block += 1  # 0 means rules, 1 your ticket, 2 nearby
        continue

    if block == 0:
        # Rules
        # print(line)
        xs = [int(x) for x in re.findall("\d+", line)]
        for i in range(0, len(xs), 2):
            for j in range(xs[i], xs[i + 1] + 1):
                valid[j] = True
    elif block == 1:
        # Your ticket
        print("your")
        # print(line)
    else:
        xs = [int(x) for x in re.findall("\d+", line)]
        for x in xs:
            if x not in valid:
                p1 += x

# print(valid)
print("p1:", p1)  # 20060 Correct
