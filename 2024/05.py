import sys
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "05.in"
data = open(filename).read().strip()
lines = [x for x in data.split("\n")]


rules: defaultdict[int, list[int]] = defaultdict()
p1, p2 = 0, 0


def must_before(fst: int, snd: int):
    if snd in rules.get(fst, []):
        return True
    return False


def valid(update: list[int]) -> bool:
    for i, x in enumerate(update):
        # For every page check the pages after and see if any of them must come
        # before the current one.
        for y in update[i + 1 :]:
            if must_before(y, x):
                return False

    return True


def make_correction(update: list[int]) -> list[int]:
    i = 0
    while i < len(update):
        moved = False
        for y in update[i + 1 :]:
            x = update[i]
            # If violating rule fix it and then check again from the same idx
            # since that idx now has a new value
            if must_before(y, x):
                y_idx = update.index(y)
                update.pop(y_idx)
                update.insert(i, y)
                moved = True
                break

        # Only proceed if no move made
        if not moved:
            i += 1

    return update


R = True
for line in lines:
    if line == "":
        R = False
        continue

    if R:
        # Parse rules
        fst, snd = map(int, line.split("|"))
        r = rules.get(fst, [])
        r.append(snd)
        rules[fst] = r
    else:
        # Check updates
        line = [int(x) for x in line.split(",")]
        if valid(line):
            p1 += line[len(line) // 2]
        else:
            c = make_correction(line)
            p2 += c[len(c) // 2]


print(p1)
print(p2)
