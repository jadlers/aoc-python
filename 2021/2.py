import fileinput

coll = {
    "aim": 0,
    "forward": 0,
    "down": 0,
}


lines = [x.strip() for x in fileinput.input()]
for line in lines:
    dir, dist = line.split(" ")
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


# commands = [(dir, int(dist) for (dir, dist) in lines]
# lines = [[(y[0], y[1]) for y in x.strip().split()] for x in fileinput.input()]
print(lines)
print(coll)

p2 = coll["forward"] * (coll["down"] - coll["up"])
print(f"p2={p2}")
