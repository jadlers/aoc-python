import sys
import re

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "15.in"
p1 = 0
p2 = 0
data = open(filename).read().strip()
X = [x.strip() for x in open(filename)]

digits = re.compile(r"\d+")
rows = {}

max_mh = 0
min_r = 0
max_r = 0
min_c = 0
max_c = 0
sensor = []
beacon = []
dists = []

r = 10 if filename == "15.ex" else 2000000
special = set()

for i, line in enumerate(X):
    # print(f"line {i} out of {len(X)}")
    sc, sr, bc, br = [int(x) for x in re.findall(r"\d+", line)]
    dr = abs(sr - br)
    dc = abs(sc - bc)
    mh = dr + dc
    sensor.append((sr, sc))
    beacon.append((br, bc))
    dists.append(mh)

    min_r = min(min_r, sr)
    max_r = max(max_r, sr)
    min_c = min(min_c, sc)
    max_c = max(max_c, sc)
    max_mh = max(max_mh, mh)

    # print((sr, sc), "from", sr - dr, "to", sr + dr)
    # if sr == 11 and sc == 0:
    #     print("missing", (sr - mh), r, (sr + mh))

    if (sr - mh) <= r <= (sr + mh):
        # print((sr, sc), f"touch special row ({r}) with mh: {mh}")
        v_dist = abs(sr - r)
        # print(f"vert dist to {r}:", v_dist)
        cov_start = sc - (mh - v_dist)
        cov_end = sc + (mh - v_dist)
        # print(cov_start, cov_end)
        for covered in range(cov_start, cov_end):
            # print("adding", covered)
            special.add(covered)
        if cov_start == cov_end:  # Does this happen?
            special.add(cov_start)

        # print("row dist to special row", abs(sr - mh), abs(abs(sr - mh) - r))

    # if sr == 8 and sc == 7:
    #     print("This:")
    # print((sr, sc), (br, bc), (dr, dc), mh)  # Only care about dr for now


# Draw edges of areas covered? Or go through each point on a line within the max_mh?

print(f"r: {min_r} -> {max_r}, c: {min_c} -> {max_c}")
print(max_mh)

# Go through all points on the row we're looking at
# r = 2000000 if filename == "15.in" else 10
# print("will iterate", abs(min_c - max_mh) + max_c + max_mh + 1)
# for c in range(min_c - max_mh, max_c + max_mh + 1):
#     if c % 250_000 == 0:
#         print(c)
#     for i, (sr, sc) in enumerate(sensor):
#         if (abs(sr-r) + abs(sc-c)) <= dists[i]:
#             # print((r,c), "within range of", (sr,sc))
#             p1+=1
#             break


# Mark edges of beacons instead?
# 1. Find range of each beacon, this method doesn't work.
# NOTE: Seems like you can only go from each sensor and not calculate the area
# a beacon covers.
# bs = {}  # pos -> dist
# for i, b in enumerate(beacon):
#     if b not in bs:
#         bs[b] = dists[i]
#     elif dists[i] > bs[b]:
#         bs[b] = dists[i]

# print(len(bs), bs)


# r = 2000000 if filename == "15.in" else 10
# for c in range(min_c - max_mh, max_c + max_mh + 1):
#     if c % 250_000 == 0:
#         print(c)
#     for b in bs:
#         br, bc = b
#         bd = bs[b]
#         if (abs(br - r) + abs(bc - c)) <= bd:
#             print((r, c), "within range of", (br, bc))
#             p1 += 1
#             break

# 2. Draw
# for pos_c in range(sc - mh, sc + mh + 1):
#     for pos_r in range(sc - mh, sc + mh + 1):
#         ddr = abs(sr - pos_r)
#         ddc = abs(sc - pos_c)
#         if ddr + ddc > mh:
#             continue

#         if sr not in rows:
#             rows[sr] = set()
#         rows[sr].add(pos_c)

# for row in rows:
#     if row == 10:
#         assert len(rows[row]) == 26, f"{len(rows[row])} {rows[row]}"
#     if row == 2000000:
#         p1 = len(rows[row])

p1 = len(special)
# print(special)
print(f"p1={p1}")  # Not: 5387315, 5387314, 3769203, 3769204
print(f"p2={p2}")
