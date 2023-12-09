import sys
import re
from math import gcd

filename = sys.argv[1] if len(sys.argv) > 1 else "8.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]
iss = [x.split()[0] for x in X[0]]

p1, p2 = 0, 0

map = {}
S = []
r = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
for i, line in enumerate(X[2:]):
    m = r.match(line)
    assert m != None
    groups = m.groups()
    node, left, right = groups
    map[node] = [left, right]
    if node[2] == "A":  # Start nodes in part 2
        S.append(node)


# Part 1
pos = "AAA"
p = 0
while True:
    i = iss[p]
    p = (p + 1) % len(iss)
    p1 += 1
    pos = map[pos][0 if i == "L" else 1]
    if pos == "ZZZ":
        break

# Part 2
# Find cycle length of all starting positions
dists = []
for pos in S:
    steps = 0
    p = 0
    while True:
        steps += 1
        i = iss[p]
        p = (p + 1) % len(iss)
        pos = map[pos][0 if i == "L" else 1]
        if pos[2] == "Z":
            dists.append(steps)
            break

# Calculate the lowest common multiple
# https://stackoverflow.com/a/42472824
lcm = 1
for i in dists:
    lcm = lcm * i // gcd(lcm, i)
p2 = lcm


print(p1)
print(p2)
