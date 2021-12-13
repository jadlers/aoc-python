import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "13.in"

p1 = 0
dots = []
C = 0
R = 0

# Parse input
coords = True
folds = []
for line in open(filename):
    if line == "\n":
        coords = False
        continue
    if coords:
        c, r = [int(x) for x in line.strip().split(",")]
        if c >= C:
            C = c +1
        if r >= R:
            R = r+1
        dots.append((r, c))
    else:
        along, val = line.strip().split()[-1].split("=")
        val = int(val)
        folds.append((along, val))

# Fill grid
G = [[0 for _ in range(C)] for _ in range(R)]
for r, c in dots:
    G[r][c] = 1


# Print the paper like in descriptions
def show():
    global G
    for row in G:
        print("".join(["#" if p else "." for p in row]))


def fold(G, along, pos):
    """Fold the paper.

    Note, not always along middle so assume remaining is just empty paper i.e.
    0 for columns and [0, ..., 0] for rows."""
    nG = []
    if along == "y":
        for i, row1 in enumerate(G[:pos]):
            row2 = G[2*pos - i] if 2*pos - i < R else [0 for _ in range(C)]
            nr = []
            for c in range(C):
                nr.append(1 if row1[c] == 1 or row2[c] == 1 else 0)
            nG.append(nr)
    elif along == "x":
        nG = []
        for row in G:
            nr = []
            for i in range(pos):
                c1 = row[i]
                c2 = row[2*pos-i] if C > 2*pos-i else 0
                nr.append(1 if c1 == 1 or c2 == 1 else 0)
            nG.append(nr)

    return nG


for along, pos in folds:
    print(f"folding along {along} at {pos}, R={R} C={C}")
    G = fold(G, along, pos)
    R = len(G)
    C = len(G[0])
    if p1 == 0:
        p1 = sum([sum(r) for r in G])

print(f"p1={p1}")
print(f"p2 8 capital letters:")
show()
