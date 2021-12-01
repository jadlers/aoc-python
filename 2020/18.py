#!/usr/bin/env python3

from functools import reduce
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
    # print(f"lhs={lhs} op={op} rhs={rhs}")
    if not lhs:
        return rhs, None

    if op == "+":
        lhs += rhs
        return lhs, None
    elif op == "*":
        return rhs, lhs


def calc(exp, start_i=None):
    # print(f"exp: {exp}, start_i={start_i}")
    i = 0
    lhs = None
    op = None
    mul_nums = []

    while i < len(exp):
        e = exp[i]
        if e == "(":
            # Evaluate a sub expression
            # print(f"begin sub expression, lhs={lhs} op={op}")
            rhs, i = calc(exp[i + 1 :], i)
            lhs, mul = apply(lhs, op, rhs)
            # print(lhs, mul)
            if mul:
                mul_nums.append(mul)

        elif start_i != None and e == ")":
            # print("end of this exp at", i)

            mul_nums.append(lhs)
            if len(mul_nums) > 1:
                lhs = reduce(lambda x, y: x * y, mul_nums)
            return lhs, start_i + i + 1
        elif e in ["*", "+"]:
            # Set operation
            op = e
        else:
            rhs = int(e)
            lhs, mul = apply(lhs, op, rhs)
            # print(lhs, mul)
            if mul:
                mul_nums.append(mul)

        # print(f"lhs={lhs} op={op} rhs={rhs}")
        i += 1

    mul_nums.append(lhs)

    # print(mul_nums)
    res = reduce(lambda x, y: x * y, mul_nums)
    return res, None


# print(calc(s))
# sys.exit(0)

p1 = 0
for line in lines:
    # print("Calculating line", line)
    c, _ = calc(line)
    print(c)
    p1 += c

# 1252139 too low
print("p1:", p1)

# p2: 65658760783597
