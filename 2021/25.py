import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "25.in"

p1 = 1
p2 = 0

rows = [[ch for ch in row.strip()] for row in open(filename).readlines()]
R = len(rows)
C = len(rows[0])


def pp(move=""):
    global rows
    print(f"Move: {move}")
    for row in rows:
        for c in row:
            print(c, end="")
        print()


def get(rows, coord):
    row, col = coord
    return rows[row][col]


def move_hor(rows):
    moved = 0
    for row in rows:
        can_move = [False for _ in row]
        for i in range(C):
            cur, next = row[i], row[(i + 1) % C]
            if cur == ">" and next == ".":
                can_move[i] = True

        for i, movable in enumerate(can_move):
            if movable:
                row[i] = "."
                row[(i + 1) % C] = ">"
                moved += 1

    return moved


def move_ver(rows):
    moved = 0
    can_move = [[False for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            cur, next = (r, c), ((r + 1) % R, c)
            if get(rows, cur) == "v" and get(rows, next) == ".":
                can_move[r][c] = True

    for r in range(R):
        for c in range(C):
            if can_move[r][c]:
                cur, next = (r, c), ((r + 1) % R, c)
                rows[r][c] = "."
                rows[(r + 1) % R][c] = "v"
                moved += 1

    return moved


def step(rows):
    mh = move_hor(rows)
    mv = move_ver(rows)

    return False if mh == 0 and mv == 0 else True


while step(rows):
    p1 += 1


print(f"p1={p1}")
print(f"p2={p2}")
