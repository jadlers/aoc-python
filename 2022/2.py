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

name = {1: "rock", 2: "papr", 3: "scis"}

for line in open(filename):
    round = 0
    [op, me] = [x.strip() for x in line.strip().split(" ")]
    play = map.get(me, 0)  # one you play

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
        # print(map[op], chosen)

    p2 += chosen

    diff = map[me] - map[op]
    # print(name[map[op]], name[map[me]], diff)
    outcome = 0
    if diff == 0:
        outcome = 3
    elif diff == 1 or diff == -2:
        outcome += 6

    round += play
    round += outcome
    # print(f"{name[map[op]]} {name[map[me]]}, {play} + {outcome} ({diff}) = {round}")
    p1 += round

print(f"p1={p1}")  # 12231, 10893
print(f"p2={p2}")  # 6459
