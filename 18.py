#!/usr/bin/env python3

import fileinput
import sys

lines = [[y for y in x.strip() if y != " "] for x in fileinput.input()]
p1 = 0

# s = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
# # s = "1 + (2 * 3) + (4 * (5 + 6))"
s = "1 + 2 * 3 + 4 * 5 + 6"
s = [y for y in s if y != " "]
# print(s)


def apply(lhs, op, rhs):
    if not lhs:
        return rhs

    # print(f"lhs={lhs} op={op} rhs={rhs}")
    if op == "+":
        lhs += rhs
        return lhs
    elif op == "*":
        lhs *= rhs
        return lhs

    assert False


def calc(exp, start_i=None):
    # print(f"exp: {exp}, start_i={start_i}")
    i = 0
    lhs = None
    op = None

    while i < len(exp):
        e = exp[i]
        if e == "(":
            # Evaluate a sub expression
            # print(f"begin sub expression, lhs={lhs} op={op}")
            rhs, i = calc(exp[i + 1 :], i)
            lhs = apply(lhs, op, rhs)

        elif start_i != None and e == ")":
            # print("end of this exp at", i)
            return lhs, start_i + i + 1
        elif e in ["*", "+"]:
            # Set operation
            op = e
        else:
            rhs = int(e)
            lhs = apply(lhs, op, rhs)

        i += 1

    return lhs, None


print(calc(s))
sys.exit(0)

p1 = 0
for line in lines:
    # print("Calculating line", line)
    c, _ = calc(line)
    print(c)
    p1 += c

print("p1:", p1)
