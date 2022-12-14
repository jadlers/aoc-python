import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "14.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]
M = {}
min_c = 500
max_c = 500
max_r = 0

for i, line in enumerate(X):
    coords = [x.strip() for x in line.split("->")]
    last: None | tuple[int, int] = None
    for coord in coords:
        c, r = [int(x) for x in coord.split(",")]
        if last != None:
            if r == last[0]:  # Horizontal
                start = min(c, last[1])
                end = max(c, last[1])
                for cc in range(start, end + 1):
                    M[(r, cc)] = "#"
            else:  # Vertical
                start = min(r, last[0])
                end = max(r, last[0])
                for rr in range(start, end + 1):
                    M[(rr, c)] = "#"

        last = (r, c)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
        max_r = max(max_r, r)

FLOOR = max_r + 2


def pmap(left=0, right=0):
    global M
    print(min_c, max_c)
    for r in range(max_r + 2):
        print(
            # f"{r+1} ",
            "".join(
                [
                    M[(r, c)] if (r, c) in M else "."
                    for c in range(min_c - left, max_c + 1 + right)
                ]
            ),
        )
    print("#" * (max_c - min_c + left + right + 1))


D = [(1, 0), (1, -1), (1, 1)]  # (r,c), down, down-left, down-right


def drop(part: int):
    global M

    grain = (0, 500)
    while True:
        r, c = grain

        if part == 2 and (0, 500) in M:
            return False  # filled to top
        for dr, dc in D:
            rr = r + dr
            cc = c + dc

            # Free to be placed there
            if (rr, cc) not in M and (part == 1 or rr != FLOOR):
                grain = (rr, cc)
                break
        if (r, c) == grain:  # it's found a place to stay
            M[(r, c)] = "o"
            return True

        # Part 1
        elif part == 1 and grain[0] > max_r:
            return False  # Could not drop


def count_grains():
    global M
    v = 0
    for coord in M:
        if M[coord] == "o":
            v += 1
    return v


# Run simulation
for part in [1, 2]:
    while True:
        success = drop(part)
        if not success:
            break
    pmap()
    print(f"p{part}={count_grains()}")
