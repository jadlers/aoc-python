import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0


xs = [int(x) for x in open(filename).readline().strip().split(",")]
hi = max(xs)

dist = []
for i in range(hi):
    i += 1
    dist.append(sum([abs(j - i) for j in xs]))


p1 = min(dist)


# NOT 479665
print(f"p1={p1}")
print(f"p2={p2}")
