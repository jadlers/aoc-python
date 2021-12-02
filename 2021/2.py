import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"

coll = {
    "aim": 0,
    "forward": 0,
    "down": 0,
}

for line in open(filename):
    dir, dist = line.strip().split()
    dist = int(dist)

    if dir not in coll:
        coll[dir] = 0

    if dir == "forward":
        coll["forward"] += dist
        coll["down"] += coll["aim"] * dist
    elif dir == "down":
        coll["aim"] += dist
    elif dir == "up":
        coll["aim"] -= dist

    print(dir, dist)
    print(coll)


print(coll)

p2 = coll["forward"] * (coll["down"] - coll["up"])
print(f"p2={p2}")
