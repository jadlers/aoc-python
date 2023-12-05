import sys
from math import inf

filename = sys.argv[1] if len(sys.argv) > 1 else "5.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n\n")]

p1, p2 = inf, 0

seeds = []
names = []
# NOTE: If missing in map, src = dst
maps = []

# Fill mappings
for i, group in enumerate(X):
    # print(f"group {i}/{len(X)}")
    if i == 0:
        seeds = [int(x) for x in group.split(":")[1].strip().split()]
        continue

    gmap = []
    for j, line in enumerate(group.split("\n")):
        if j == 0:
            names.append(line.split()[0])
            continue

        dst_start, src_start, length = [int(x) for x in line.split()]
        # print(line, src_start, dst_start, len)

        ds, de = dst_start, dst_start + length - 1
        ss, se = src_start, src_start + length - 1
        gmap.append([ds, de, ss, se])

    maps.append(gmap)


def find_location(seed):
    for map in maps:
        for r in map:
            ds, _, ss, se = r
            if ss <= seed <= se:

                seed = ds + (seed - ss)
                break

    return seed


for seed in seeds:
    p1 = min(p1, find_location(seed))


print(p1)
print(p2)
