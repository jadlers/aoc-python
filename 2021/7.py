import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = []
p2 = []

def dist_cost(n):
    return n*(n+1)/2 # Compute instead of store

xs = [int(x) for x in open(filename).readline().strip().split(",")]
hi = max(xs)

dist = []
for i in range(hi):
    i += 1
    p1.append(sum([abs(j - i) for j in xs]))
    p2.append(sum([dist_cost(abs(j - i)) for j in xs]))


p1 = min(p1)
p2 = int(min(p2))

# NOT 479665
print(f"p1={p1}")
print(f"p2={p2}")
