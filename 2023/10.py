import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "10.in"
data = open(filename).read().strip()
X = [[y.split()[0] for y in x.strip()] for x in data.split("\n")]

p1, p2 = 0, 0


def find_start():
    for row, line in enumerate(X):
        for col, ch in enumerate(line):
            if ch == "S":
                return (row, col)
    assert False, f"no start"


# For finding connecting pipes from S
valid = {
    # From below going up
    "u": ["|", "7", "F", "S"],
    # From left going right
    "r": ["-", "J", "7", "S"],
    # From above going down
    "d": ["|", "L", "J", "S"],
    # From right going left
    "l": ["-", "F", "L", "S"],
}

# Can be used for printing sample maps
# M = [["." for _ in range(len(X[0]))] for _ in range(len(X))]

# keep track of where we've been already
visited = {}
r, c = find_start()
S = (r, c)

# find two adjacent starting points
D = []
for dir, dr, dc in [["u", -1, 0], ["r", 0, 1], ["d", 1, 0], ["l", 0, -1]]:
    rr = r + dr
    cc = c + dc
    if rr < 0 or rr >= len(X):
        continue
    elif cc < 0 or cc >= len(X[0]):
        continue
    # print(dir, "at", (rr, cc), X[rr][cc])
    if X[rr][cc] in valid[dir] and (rr, cc) not in visited:
        # print("add neighbor", (rr, cc), X[rr][cc])
        D.append((rr, cc))


def next_from_pipe(delta, cur_pipe):
    """
    delta for which the direction the pipe got to the current one from the
    previous. With the row: "--J" next_from_pipe(delta=(0,1), cur_pipe="J") is
    expected to be (-1,0) since the previous came from the left, is now at "J"
    and will continue up.
    """
    dr, dc = delta
    if cur_pipe == "-":
        assert dr == 0
        return (0, 1) if dc == 1 else (0, -1)
    elif cur_pipe == "|":
        assert dc == 0
        return (1, 0) if dr == 1 else (-1, 0)
    elif cur_pipe == "7":
        return (1, 0) if dr == 0 and dc == 1 else (0, -1)
    elif cur_pipe == "L":
        return (0, 1) if dr == 1 and dc == 0 else (-1, 0)
    elif cur_pipe == "J":
        return (0, -1) if dr == 1 and dc == 0 else (-1, 0)
    elif cur_pipe == "F":
        return (0, 1) if dr == -1 and dc == 0 else (1, 0)
    assert False, f"{delta} {cur_pipe}"


def get_next(prev, cur):
    pr, pc = prev
    cr, cc = cur
    cur_pipe = X[cr][cc]
    dr, dc = cr - pr, cc - pc
    return next_from_pipe((dr, dc), cur_pipe)


D1, D2 = [S, D[0]], [S, D[1]]


def find_end():
    for _ in range(100_000):
        for i, path in enumerate([D1, D2]):
            r, c = path[-1]
            dr, dc = get_next(path[-2], path[-1])
            next = (r + dr, c + dc)
            path.append(next)
            if i == 0 and D2[-1] == next:
                return len(D1) - 1
            elif i == 1 and D1[-1] == next:
                return len(D2) - 1


p1 = find_end()
print(p1)  # Not 49, it's: 6846
print(p2)
