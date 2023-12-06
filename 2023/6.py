from collections import defaultdict
from functools import reduce
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "6.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

p1, p2 = 1, 0

ts = [int(x) for x in X[0].split()[1:]]
ds = [int(x) for x in X[1].split()[1:]]


def victories(time, dist):
    for h in range(time):
        d = h * (time - h)
        if d > dist:
            w = (time + 1) - (h * 2)
            return w


wins = defaultdict(int)
for i, t in enumerate(ts):
    won = False
    for h in range(t):
        d = h * (t - h)
        if d > ds[i]:
            w = (t + 1) - (h * 2)
            wins[i] = w
            break

for w in wins.values():
    p1 *= w

t2 = int(reduce(lambda acc, cur: acc + cur, [str(t) for t in ts]))
d2 = int(reduce(lambda acc, cur: acc + cur, [str(d) for d in ds]))
p2 = victories(t2, d2)


print(p1)
print(p2)
