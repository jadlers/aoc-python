import sys
from math import floor

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "3.in"
p1 = 0
p2 = 0

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert len(letters) == 52

# calculate value
def dup_points(ch_set: set) -> int:
    # print(f'calculate points for {ch_set}')
    points = [letters.index(ch)+1 for ch in "".join(ch_set)]
    # print(ch_set)
    # print(points, sum(points))
    return sum(points)


for line in open(filename):
    line = line.strip()
    a, b = line[: floor(len(line) / 2)], line[floor(len(line) / 2) :]
    # print(a, " ", b)
    dup1 = set()
    for ch in a:
        res = [x for x in filter(lambda x: x == ch, b)]
        for dch in res:
            dup1.add(dch)

    p1 += dup_points(dup1)
    # print(dup2)


# p1 = sum(points)
# print(dup2)


print(f"p1={p1}")  # 12231, 10893
print(f"p2={p2}")  # 6459
