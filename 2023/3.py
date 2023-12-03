import re
import sys
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "3.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

R = len(X)
C = len(X[0])

p1, p2 = 0, 0

rdigit = re.compile(r"(\d+)")
rsymbol = re.compile(r"([^\d\.])")

# numbers parsed
N: list[int] = []
# (r,c) => number index in N
M = defaultdict(int)
# Location of all symbols [(r,c)]
S = []

for r, line in enumerate(X):
    # Parse out numbers with position
    c = 0
    while c < C:
        m = rdigit.search(line, c)
        if not m:
            break

        n_idx = len(N)
        N.append(int(m.group(0)))
        s, e = m.span()
        for c2 in range(s, e):
            M[(r, c2)] = n_idx
        c = e

    # Parse out symbols with position
    c = 0
    while c < C:
        m = rsymbol.search(line, c)
        if not m:
            break

        s, e = m.span()
        S.append((r, s))
        c = e

# True for indicies in N which should be included
include = [False for _ in N]

# Go through all symbols and mark adjacent numbers as included
for (r, c) in S:
    matched: set[int] = set()
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = r + dr
            cc = c + dc
            if not (0 <= rr < R) or not (0 <= cc < C):
                continue

            # mark number as included
            adj_num = M.get((rr, cc))
            if adj_num is not None:
                include[adj_num] = True
                if X[r][c] == "*":
                    matched.add(adj_num)
    # p2
    if len(matched) == 2:
        n1, n2 = N[matched.pop()], N[matched.pop()]
        p2 += n1 * n2


parts = [x for i, x in enumerate(N) if include[i]]
p1 = sum(parts)


print(p1)
print(p2)
