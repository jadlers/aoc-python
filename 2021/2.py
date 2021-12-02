import fileinput

coll = {}

lines = [x.strip() for x in fileinput.input()]
for line in lines:
    dir, dist = line.split()
    if dir not in coll:
        coll[dir] = 0
    print(dir, dist)
    coll[dir] += int(dist)

# commands = [(dir, int(dist) for (dir, dist) in lines]
# lines = [[(y[0], y[1]) for y in x.strip().split()] for x in fileinput.input()]
print(lines)
print(coll)

p1 = coll["forward"] * (coll["down"] - coll["up"])
print(f"p1={p1}")
