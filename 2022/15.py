import sys
import re

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "15.in"
example_input = filename == "15.ex"
p1 = 0
p2 = 0
data = open(filename).read().strip()
X = [x.strip() for x in open(filename)]

max_xy = 20 if example_input else 4000000
rows = [[] for _ in range(max_xy + 1)]

special_r = 10 if example_input else 2000000
special = set()  # Used to get P1 `r`

M = [["." for _ in range(21)] for _ in range(21)]


for i, line in enumerate(X):
    print(f"line {i} out of {len(X)}")
    sc, sr, bc, br = [int(x) for x in re.findall(r"\d+", line)]
    dr = abs(sr - br)
    dc = abs(sc - bc)
    mh = dr + dc
    if 0 <= sr <= 20 and 0 <= sc <= 20:
        M[sr][sc] = "S"
    if 0 <= br <= 20 and 0 <= bc <= 20:
        M[br][bc] = "B"

    # Goes through the special row for P1
    # How to generalize and do similar for every row?
    for r in range(sr - mh, sr + mh + 1):
        if not (0 <= r <= max_xy):
            continue

        # How far from sensor the current row is
        v_dist = abs(sr - r)
        # print(f"vert dist to {r}:", v_dist)
        cov_start = sc - (mh - v_dist)
        cov_end = sc + (mh - v_dist)
        assert mh >= v_dist, f"mh={mh} v_dist={v_dist}"

        if r == 0:
            print("touches row 0", (sr,sc), mh, v_dist, )

        if example_input and (7, 8) == (sr, sc):
            for c in range(max(0, cov_start), min(21, cov_end + 1)):
                if M[r][c] == ".":
                    M[r][c] = "#"

        rows[r].append((max(0, cov_start), min(cov_end, max_xy)))

        # For calculating P1, can probably be updated once P2 is complete
        if r == special_r:
            for covered in range(cov_start, cov_end):
                # print("adding", covered)
                special.add(covered)
            if cov_start == cov_end:  # Does this happen?
                special.add(cov_start)

        # print("row dist to special row", abs(sr - mh), abs(abs(sr - mh) - r))

    # if sr == 8 and sc == 7:
    #     print("This:")
    # print((sr, sc), (br, bc), (dr, dc), mh)  # Only care about dr for now

# Only print on example, real is way too big
if example_input:
    for i, Mr in enumerate(M):
        print("".join(Mr), i)


def find_beacon(row, cr):
    rs = None  # row start (x value on row y)
    ce = 0  # current end
    for s, e in row:
        # print(s, e, ce)
        if rs == None:  # First coverage tuple
            assert s == 0, f"{s} {row}"
            rs = s
            ce = e
            continue
        if s > ce:
            print(ord_row)
            print("found it!", (cr, ce + 1))
            return (cr, ce + 1)
            # print((ce + 1) * 4000000 + cr)
            # assert False
        ce = max(ce, e)


candidates = []
for cr in range(0, 400_000):  # max_r):
    if cr % 10_000 == 0:
        print("on row", cr)

    ord_row = sorted(rows[cr], key=lambda x: x[0])
    candidate = find_beacon(ord_row, cr)
    if candidate:
        print(candidate)
        p2 = candidate[1] * 4_000_000 + candidate[0]
        break
        # candidates.append(candidate)
    # print(ord_row)


# print(candidates)

# Draw edges of areas covered? Or go through each point on a line within the max_mh?

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
if example_input:
    assert p1 == 26
else:
    assert p1 == 4985193
print(f"p2={p2}")  # Not: 2622236000000
if example_input:
    assert p2 == 56000011
