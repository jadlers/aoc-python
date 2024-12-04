import sys
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "04.in"
data = open(filename).read().strip()
R = [x for x in data.split("\n")]

MR = len(R)
MC = len(R[0])

p1, p2 = 0, 0


M = defaultdict()
for r, row in enumerate(R):
    for c, char in enumerate(row):
        M[(r, c)] = char


# print(M)
def search(at: tuple[int, int], dir: tuple[int, int]) -> bool:
    """
    Search for 4 chars in one direction. Return true if the chars are "XMAS" in
    order. Break early if we end up outside the board.
    """
    r, c = at
    dr, dc = dir

    txt = []
    for _ in range(4):
        ch = M.get((r, c))
        # print((r,c), (dr,dc), ch)
        if ch == None:
            return False
        txt.append(ch)
        r += dr
        c += dc

    # print("".join(txt))
    return "".join(txt) == "XMAS"


def square_search(at: tuple[int, int]) -> bool:
    """
    M.S    s.t
    .A. -> .@.  We're at @
    M.S    u.v
    """
    r, c = at
    s = M.get((r - 1, c - 1))
    t = M.get((r - 1, c + 1))
    u = M.get((r + 1, c - 1))
    v = M.get((r + 1, c + 1))
    if len([x for x in [s, t, u, v] if x != None]) != 4:
        return False

    if not ((s == "M" and v == "S") or (s == "S" and v == "M")):
        return False
    if not ((t == "M" and u == "S") or (t == "S" and u == "M")):
        return False

    return True


for r in range(MR):
    for c in range(MC):
        if R[r][c] == "X":
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue

                    if search((r, c), (dr, dc)):
                        p1 += 1

        if R[r][c] == "A":
            if square_search((r, c)):
                p2 += 1

print(p1)
print(p2)
