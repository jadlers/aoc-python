#!/usr/bin/env python3

import fileinput
import re

lines = [x.strip() for x in fileinput.input()]
lines.append("")  # To mach the last passport


def has_key(d, key):
    if d.get(key) != None:
        return True
    return False


def required_fields(fields):
    if len(fields) < 7:
        return False
    elif len(fields) == 7 and has_key(fields, "cid"):
        return False
    return True


def valid_p1(fields):
    if required_fields(fields):
        return True
    return False


def in_range(val, lo, hi):
    if val < lo:
        return False
    elif val > hi:
        return False
    return True


def valid_p2(fields):
    if not required_fields(fields):
        return False

    for k in fields:
        v = fields[k]

        if k == "byr":
            year = int(v)
            if not in_range(year, 1920, 2002):
                return False
        elif k == "iyr":
            year = int(v)
            if not in_range(year, 2010, 2020):
                return False
        elif k == "eyr":
            year = int(v)
            if not in_range(year, 2020, 2030):
                return False
        elif k == "hgt":
            r = re.search("(\d+)(in|cm)", v)
            if r == None:
                return False
            l = int(r.group(1))
            if r.group(2) == "cm":
                if not in_range(l, 150, 193):
                    return False
            else:
                if not in_range(l, 59, 76):
                    return False
        elif k == "hcl":
            if not re.search("#[a-f0-9]{6}", v):
                return False
        elif k == "ecl":
            if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif k == "pid":
            if len(v) != 9:
                return False
            elif len(v) == 9 and not re.search("\d{9}", v):
                return False

    return True


fields = {}
has_cid = False

p1 = 0
p2 = 0
for line in lines:
    if line == "":  # New passport
        if valid_p1(fields):
            p1 += 1
        if valid_p2(fields):
            p2 += 1

        fields = {}
        has_cid = False
        continue

    parts = line.split(" ")
    for p in parts:
        (k, v) = p.split(":")
        fields[k] = v


print("p1:", p1)  # 249 too low, 250 correct
print("p2:", p2)  # 160 too high
