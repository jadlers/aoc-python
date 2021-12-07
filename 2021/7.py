import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

C = {}
def dist_cost(n):
    if n in C:
        return C[n]
    res = 0
    for i in range(n):
        res += i+1

    C[n] = res
    return res

xs = [int(x) for x in open(filename).readline().strip().split(",")]
hi = max(xs)

dist = []
for i in range(hi):
    i += 1
    dist.append(sum([dist_cost(abs(j - i)) for j in xs]))


p1 = min(dist)

# print(dist_cost(1))
# print(dist_cost(2))
# print(dist_cost(3))
# print(dist_cost(4))


# NOT 479665
print(f"p1={p1}")
print(f"p2={p2}")
