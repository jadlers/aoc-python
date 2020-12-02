#!/usr/bin/env python3

import fileinput
import re

valid = 0


def p1():
    p = re.compile("(\d+)-(\d+) ([a-z]): (\w+)")
    xs = [x for x in fileinput.input()]
    for x in xs:
        res = p.match(x)
        start = int(res.group(1))
        end = int(res.group(2))
        letter = res.group(3)
        pw = res.group(4)

        searched = [x for x in pw if x == letter]

        if len(searched) >= start and len(searched) <= end:
            valid += 1
            print(x)


def p2():
    global valid
    p = re.compile("(\d+)-(\d+) ([a-z]): (\w+)")
    xs = [x for x in fileinput.input()]
    for x in xs:
        res = p.match(x)
        start = int(res.group(1)) - 1
        end = int(res.group(2)) - 1
        letter = res.group(3)
        pw = res.group(4)

        searched = [x for x in pw if x == letter]
        lval = 0
        print(start, end, pw)
        if pw[start] == letter:
            lval += 1
        if pw[end] == letter:
            lval += 1

        if lval == 1:
            valid += 1


p2()
print(valid)
