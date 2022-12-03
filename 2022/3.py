import sys
from math import floor

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "3.in"
X = [x.strip() for x in open(filename)]
p1 = 0
p2 = 0

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert len(letters) == 52

# calculate value
def dup_points(ch_set: set) -> int:
    """calulate value of the letters in `ch_set`.

    - Lowercase item types `a` through `z` have priorities 1 through 26.
    - Uppercase item types `A` through `Z` have priorities 27 through 52.
    """
    points = [letters.index(ch) + 1 for ch in "".join(ch_set)]
    return sum(points)


last_group = -1
common = set(letters)
for (idx, line) in enumerate(X):
    # Part 1
    half = floor(len(line) / 2)
    a, b = line[:half], line[half:]
    dup1 = set()
    for ch in a:
        res = [x for x in filter(lambda x: x == ch, b)]
        for dch in res:
            dup1.add(dch)

    p1 += dup_points(dup1)

    # Part 2
    group = floor(idx / 3)
    if last_group != group and last_group >= 0:
        assert len(common) == 1
        p2 += letters.index(common.pop()) + 1
        common = set(letters)
    common &= set(line)

    last_group = group

# Part 2
p2 += letters.index(common.pop()) + 1


print(f"p1={p1}")  # 12231, 10893
print(f"p2={p2}")  # 6459
