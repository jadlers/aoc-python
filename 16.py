#!/usr/bin/env python3

import fileinput
import re

lines = [x.strip() for x in fileinput.input()]

block = 0

tickets = []
valid = {}
p1 = 0
for line in lines:
    if not line:
        block += 1  # 0 means rules, 1 your ticket, 2 nearby
        continue

    if block == 0:
        # Rules
        # print(line)
        type_ = line.split(":")[0]
        xs = [int(x) for x in re.findall("\d+", line)]
        valid[type_] = {}
        for i in range(0, len(xs), 2):
            for j in range(xs[i], xs[i + 1] + 1):
                valid[type_][j] = True
    elif block == 1:
        # Your ticket
        my_ticket = [int(x) for x in re.findall("\d+", line)]
    else:
        if line.startswith("nearby"):
            continue

        ticket = [int(x) for x in re.findall("\d+", line)]
        acc = False
        for x in ticket:
            acc = False
            for rule in valid:
                if x in valid[rule]:
                    # print(f"x={x} valid in {rule}")
                    acc = True
                    break
            if not acc:
                # print(f"{x} not accepted")
                p1 += x
                break  # Invalid so throw away

        if acc:
            tickets.append(ticket)


print("p1:", p1)  # 20060 Correct


pos_rule = {rule: True for rule in valid.keys()}
possible = []
for _ in tickets[0]:
    possible.append(pos_rule.copy())

for ticket in tickets:
    for (tic_field_idx, tic_field_val) in enumerate(ticket):
        for (j, pos_field) in enumerate(possible[tic_field_idx]):
            if tic_field_val not in valid[pos_field]:
                possible[tic_field_idx][pos_field] = False

possible = [[x for x in p.keys() if p[x]] for p in possible]

while True:
    lens = [len(p) for p in possible]
    if max(lens) == 1:
        break

    for i in range(len(possible)):
        if len(possible[i]) == 1:
            determined_field = possible[i][0]
            # Remove from all other possible fields
            for j in range(len(possible)):
                if i == j:
                    continue
                if determined_field in possible[j]:
                    possible[j].remove(determined_field)

p2 = 1
for (i, rule) in enumerate(possible):
    if rule[0].startswith("departure"):
        p2 *= my_ticket[i]

# Correct 2843534243843
print("p2:", p2)
