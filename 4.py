#!/usr/bin/env python3

import fileinput

lines = [x.strip() for x in fileinput.input()]
lines.append("")

print(lines[:5])


def blank_fileds():
    return {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": False,
    }


def valid(fields, has_cid):
    if fields == 8 or (fields == 7 and not has_cid):
        return True
    return False


fields = 0
has_cid = False

p1 = 0
for line in lines:
    if line == "":  # New passport
        print(fields, has_cid)
        if valid(fields, has_cid):
            p1 += 1

        fields = 0
        has_cid = False
        continue

    parts = line.split(" ")
    print(parts)
    for p in parts:
        print("Adding", p.split(":")[0])
        fields += 1
        if p.split(":")[0] == "cid":
            has_cid = True


print(fields, has_cid)
print("p1:", p1)  # 249 too low
