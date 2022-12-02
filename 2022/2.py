import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

map = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3,
}

for line in open(filename):
    [op, me] = [x.strip() for x in line.strip().split(" ")]
    p1 += map.get(me, 0)  # one you play

    diff = map[me] - map[op]
    if diff == 0:
        p1 += 3
    elif (diff % 3) == 1:
        p1 += 6

    # P2
    chosen = -1
    if me == "X":  # lose
        chosen = map[op] - 1
    elif me == "Y":  # draw
        chosen = map[op] - 0
        p2 += 3
    elif me == "Z":  # win
        chosen = map[op] - 2
        p2 += 6
    if chosen < 1:
        chosen += 3
    p2 += chosen

print(f"p1={p1}")  # 12231, 10893
print(f"p2={p2}")  # 6459
