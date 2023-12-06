from collections import defaultdict
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "6.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

p1, p2 = 1, 0

ts = [int(x) for x in X[0].split()[1:]]
ds = [int(x) for x in X[1].split()[1:]]
print(ts, ds)

wins = defaultdict(int)
for i, t in enumerate(ts):
    for h in range(t):
        d = h * (t - h)
        if d > ds[i]:
            wins[i] += 1

for w in wins.values():
    p1 *= w

print(p1)
print(p2)
