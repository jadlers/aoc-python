import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"

lows = []
rows = []  # rows[y][x]
for line in open(filename):
    rows.append([int(x) for x in line.strip()])


def is_low(y, x):
    m = rows[y][x]
    for dy in [-1, 1]:
        if y + dy < 0 or y + dy >= len(rows):
            continue
        elif m >= rows[y + dy][x]:
            return False
    for dx in [-1, 1]:
        if x + dx < 0 or x + dx >= len(rows[0]):
            continue
        elif m >= rows[y][x + dx]:
            return False
    return True


for y in range(len(rows)):
    for x in range(len(rows[0])):
        if is_low(y, x):
            lows.append((x, y))

p1 = sum([rows[y][x] for (x,y) in lows]) + len(lows)

# For P2 do a breadth first search-ish for the low points until edge/9
def basin_size(x_init, y_init):
    marked = {}
    queue = [(x_init, y_init)]
    size = 0
    basin_coords = []
    while len(queue) > 0:
        [xc, yc] = queue[0]
        queue = queue[1:]
        size += 1  # count the location
        basin_coords.append((xc, yc))
        marked[(xc, yc)] = True

        for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            x = xc + dx
            y = yc + dy
            if (x < 0 or x >= len(rows[0])) or (y < 0 or y >= len(rows)):
                continue

            if (x, y) in marked:
                continue
            elif rows[y][x] != 9:
                marked[(x, y)] = True
                queue.append((x, y))
    return size


sizes = []
for x, y in lows:
    sizes.append(basin_size(x, y))

# product of 3 biggest basin sizes
a, b, c = sorted(sizes)[-3:]
p2 = a * b * c


print(f"p1={p1}")
print(f"p2={p2}")
