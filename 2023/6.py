from functools import reduce
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "6.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

ts = [int(x) for x in X[0].split()[1:]]
ds = [int(x) for x in X[1].split()[1:]]


def victories(time, dist):
    """
    Find the first time the time held will win the race. The last time which
    will still win has the same distance to the end of the time range as the
    first win has to the start (0).
    """
    for h in range(time):
        d = h * (time - h)
        if d > dist:
            w = (time + 1) - (h * 2)
            return w
    return 1  # when multiplied 1 is the id value


wins = [victories(t, ds[i]) for i, t in enumerate(ts)]
p1 = reduce(lambda acc, cur: acc * cur, wins)

t2 = int(reduce(lambda acc, cur: acc + cur, [str(t) for t in ts]))
d2 = int(reduce(lambda acc, cur: acc + cur, [str(d) for d in ds]))
p2 = victories(t2, d2)


print(p1)
print(p2)
