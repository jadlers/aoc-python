import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"

coll = {
    "aim": 0,
    "forward": 0,
    "down": 0,
}

# For P1
h1 = 0
v1 = 0

for line in open(filename):
    dir, dist = line.strip().split()
    dist = int(dist)

    if dir not in coll:
        coll[dir] = 0

    if dir == "forward":
        coll["forward"] += dist
        coll["down"] += coll["aim"] * dist
        h1 += dist
    elif dir == "down":
        coll["aim"] += dist
        v1 += dist
    elif dir == "up":
        coll["aim"] -= dist
        v1 -= dist


p1 = h1 * v1
p2 = coll["forward"] * (coll["down"] - coll["up"])

print(f"p1={p1}")
print(f"p2={p2}")
