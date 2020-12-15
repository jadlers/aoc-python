#!/usr/bin/env python3

import fileinput
import re


def masked_value(mask, val):
    b = bin(val)[2:]
    print(f"val={val}, b={b}")
    for i in range(len(b[2:]), 0, -1):
        print(i, mask[-i], b[-1])

    return val


def create_masks(mask):
    am = ["1" if x != "0" else "0" for x in mask]
    an = int("".join(am), 2)
    om = ["1" if x == "1" else "0" for x in mask]
    on = int("".join(om), 2)

    return an, on


# TESTS
# mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
# am, om = create_masks(mask)
# print(am, om)
# tv = 11
# tv &= am
# tv |= om
# print(tv)


mem = {}
mask = ""
and_mask, or_mask = 0, 0
for line in fileinput.input():
    if line.startswith("mask"):
        # mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
        mask = line.split(" ")[-1].strip()
        # print("Creating mask with:", mask)
        and_mask, or_mask = create_masks(mask)
        # print(and_mask, or_mask)
    else:
        # print(and_mask, or_mask)
        # mem[8] = 11
        idx, val = [int(x) for x in re.findall("\d+", line)]
        # print("pre val:", val)
        val &= and_mask
        val |= or_mask
        # print(f"mem[{idx}] = {val}")

        mem[idx] = val


p1 = 0
for (k, v) in mem.items():
    p1 += v

# 353 too low, 34054438102114 too high
print("p1:", p1)
