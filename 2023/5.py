import sys
from math import inf

filename = sys.argv[1] if len(sys.argv) > 1 else "5.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n\n")]

p1, p2 = inf, inf

seeds = []
available_seeds = []  # for P2
names = []
# NOTE: If missing in map, src = dst
maps = []

seed_loc = {}

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


def has_seed(loc):
    # print(f"has_seed({loc})")
    for i in range(len(maps) - 1, -1, -1):
        map = maps[i]
        for r in map:
            ds, de, ss, _ = r
            # print(f"step {i}, ds={ds}, loc={loc}, de={de}, ss={ss}")
            if ds <= loc <= de:
                loc = ss + (loc - ds)
                break

    # Check to see if it's in available seeds
    for seed_start, seed_end in available_seeds:
        if seed_start <= loc < seed_end:
            return loc

    return -1


for i in range(0, len(seeds), 2):
    seed_start, length = seeds[i], seeds[i + 1]
    available_seeds.append([seed_start, seed_start + length])

loc = 0
while True:
    if loc % 100_000 == 0:
        print("current location:", loc)
    seed = has_seed(loc)
    if seed != -1:
        print(seed)
        p2 = loc
        break
    loc += 1


# NOTE: Going through seeds, way too slow
# for i in range(0, len(seeds), 2):
#     print(f"{i/2}/{len(seeds)/2}")
#     seed_start, length = seeds[i], seeds[i + 1]
#     for seed in range(seed_start, seed_start + length):
#         if seed % 1_000_000 == 0:
#             print(f"\t{seed}/{seed_start+length}")
#         if seed in seed_loc:
#             continue
#         loc = find_location(seed)
#         seed_loc[seed] = loc
#         p2 = min(p2, loc)

# Do we need to go backwards? Start from location and work our way to the seed?


# P1
# for seed in seeds:
#     p1 = min(p1, find_location(seed))


print(p1)
print(p2)
