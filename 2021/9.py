import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

# dx = [-1, 1]
# dy = [-1, 1]

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
            lows.append(rows[y][x])

p1 = sum(lows) + len(lows)

print(f"p1={p1}")
print(f"p2={p2}")
