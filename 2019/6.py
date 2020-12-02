#!/usr/bin/env python3

import fileinput

# Example line: (C orbits B)
# B)C

# key: object => object key orbits around
orb_map = {}

lines = [x for x in fileinput.input()]
for line in lines:
    base, orbits = line.strip().split(")")
    orb_map[orbits] = base


# distance to COM (center of mass)
chain_lens = {}
for obj in orb_map:
    org = obj
    dist = 1
    while orb_map[obj] != "COM":
        dist += 1
        obj = orb_map[obj]

    chain_lens[org] = dist

p1 = 0
for key in chain_lens:
    num = chain_lens[key]
    p1 += num

# Find last common obj and its distance
# (YOU -> COM) + (SAN -> COM) - 2*Common


def path_to_com(obj):
    path = [obj]
    while obj != "COM":
        obj = orb_map[obj]
        path.insert(0, obj)

    return path


def common_path(a, b):
    ap = path_to_com(a)
    bp = path_to_com(b)

    for i in range(min(len(ap), len(bp))):
        if ap[i] != bp[i]:
            return ap[:i]


p_you = path_to_com("YOU")
p_san = path_to_com("SAN")
p_com = common_path("YOU", "SAN")
you_len = len(p_you) - 1
san_len = len(p_san) - 1

p2 = you_len + san_len - (2 * len(p_com))

print("p1", p1)
print("p2", p2)
