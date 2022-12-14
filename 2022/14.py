import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "14.in"
p1 = 0
p2 = 1
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
                print(f"Horizontal {last} -> {(r,c)}")
                start = min(c, last[1])
                end = max(c, last[1])
                for cc in range(start, end + 1):
                    M[(r, cc)] = "#"
            else:  # Vertical
                print(f"vertical {last} -> {(r,c)}")
                start = min(r, last[0])
                end = max(r, last[0])
                for rr in range(start, end + 1):
                    M[(rr, c)] = "#"

        last = (r, c)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
        max_r = max(max_r, r)


print(min_c, max_c, max_r)


def pmap():
    global M
    print(min_c, max_c)
    for r in range(max_r + 1):
        print(
            # f"{r+1} ",
            "".join(
                [M[(r, c)] if (r, c) in M else "." for c in range(min_c, max_c + 1)]
            ),
        )


D = [(1, 0), (1, -1), (1, 1)]  # (r,c), down, down-left, down-right


def drop():
    global M

    grain = (0, 500)
    while True:
        r, c = grain
        for dr, dc in D:
            if (r+dr, c+dc) not in M: # Free to be placed there
                grain = (r+dr, c+dc)
                # print("grain moved", (r+dr, c+dc))
                break
        if (r,c) == grain: # it's found a place to stay
            M[(r,c)] = "o"
            return True
        elif grain[0] > max_r:
            return False  # Could not drop


while True:
    success = drop()
    if not success:
        print("could not drop grain number")
        break
    # if i % 5 == 0:
    #     pmap()

pmap()
for coord in M:
    if M[coord] == "o":
        p1 += 1

print(f"p1={p1}")  # Not: 5930
print(f"p2={p2}")
