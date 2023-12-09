import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else "8.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]
iss = [x.split()[0] for x in X[0]]

p1, p2 = 0, 0

map = {}
r = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
for i, line in enumerate(X[2:]):
    m = r.match(line)
    assert m != None
    groups = m.groups()
    node, left, right = groups
    # print(line, node, left, right)
    map[node] = [left, right]


n = "AAA"
p = 0
while True:
    i = iss[p]
    p = (p + 1) % len(iss)
    p1 += 1
    n = map[n][0 if i == "L" else 1]
    if n == "ZZZ":
        break


print(p1)
print(p2)
