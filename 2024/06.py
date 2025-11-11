import sys
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "06.in"
data = open(filename).read().strip()
lines = [x for x in data.split("\n")]
p1, p2 = 0, 0

board: defaultdict[tuple[int, int], str] = defaultdict(str)
# visited: defaultdict[tuple[int, int], bool] = defaultdict(bool)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
at = (0, 0)
visited: set[tuple[int, int]] = set()
turns: set[tuple[int, int]] = set()
obstacles: set[tuple[int, int]] = set()


for r, row in enumerate(lines):
    for c in range(len(row)):
        board[(r, c)] = row[c]
        if row[c] == "^":
            at = (r, c)
            visited.add(at)


def move(at: tuple[int,int], dir: int, loop_check: bool = False) -> bool:
    r,c = at
    if (r, c) not in board:
        return False

    next = (r + dirs[dir][0], c + dirs[dir][1])
    if next not in board:
        return False
    elif board[next] == "#":
        dir = (dir + 1) % 4
        turns.add(at)
        # print(f"turn {at=}")
    elif not loop_check:
        # Simulate adding and running until exiting board or getting back to
        # the same position indicating a loop

        # Does making a turn here make me come back to a previous turn?
        pdir = (dir + 1) % 4
        # print(f"{at=} try walking in {pdir=} {dirs[pdir]=}")
        j = 0
        pat = (r, c)
        while True:
            pnext = (pat[0] + dirs[pdir][0], pat[1] + dirs[pdir][1])
            # print(f"{pnext=}")
            if pnext not in board:
                # print(f"search outside of board")
                break
            elif pat in turns and board[pnext] == "#":
                obstacles.add(next)
                # print(f"added obstacle {next=}")
                break
            elif board[pnext] == "#":
                # print(f"reached wall without previous visit at {pnext=}")
                break

            pat = pnext
            j += 1
            assert j < 100_000, "infinite loop, j"

        # print(f"{turns=} 3rd last={turns[-3]}")

        at = next
        visited.add(at)
        # print(f"now {at=}")

    return True

def loop_check(at: tuple[int,int], dir: int) -> bool:
    start = at
    r,c = at
    if (r, c) not in board:
        return False

    next = (r + dirs[dir][0], c + dirs[dir][1])
    if next not in board:
        return False
    elif board[next] == "#":
        dir = (dir + 1) % 4
        turns.add(at)
        # print(f"turn {at=}")

    return True


i = 0
while True:
    assert i < 100_000, "infinite loop, i"
    if not move(*at):
        break
    i += 1

if filename == "06.sample":
    correct = [(6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)]
    if set(correct) != obstacles:
        print("Incorrect obstacles")

p1 = len(visited)
p2 = len(obstacles)
print(p1)
print(p2)  # 388, 617 too low

# Liljevalchs   11-17 (varje dag)
# Pepparkap     10-18 (lör sön, stängt mån)
# Fotografiska  09-23 (varje dag)


# 1. (6,3)
#
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ....|..#|.
# ....|...|.
# .#.O^---+.
# ........#.
# #.........
# ......#...
# 
# 2. (7,6)
# 
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ......O.#.
# #.........
# ......#...
# 
# 3. (7,7)
# 
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----+O#.
# #+----+...
# ......#...
# 
# 4. (8,1)
# 
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ..|...|.#.
# #O+---+...
# ......#...
# 
# 5. (8,3)
# 
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ....|.|.#.
# #..O+-+...
# ......#...
# 
# 6. (9,7)
# 
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----++#.
# #+----++..
# ......#O..

