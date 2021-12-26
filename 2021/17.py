from re import findall
import sys
import os


def DEB(*args):
    if os.getenv("DEBUG"):
        print(args)


# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "25.in"

p1 = 0
p2 = 0


file_content = open(filename).read().strip()
min_x, max_x, min_y, max_y = [int(x) for x in findall("-?\\d+", file_content)]

print(min_x, max_x, min_y, max_y)


def hits_target(dx: int, dy: int):
    global min_x, max_x, min_y, max_y
    x, y, hiy = 0, 0, 0
    positions: list[tuple[int, int]] = [(x, y)]
    while y >= min_y:
        x += dx
        # Don't change dx if 0
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

        y += dy
        dy -= 1

        if y > hiy:
            hiy = y

        positions.append((x, y))
        if min_x <= x <= max_x and min_y <= y <= max_y:
            # DEB(positions)
            return True, (x, y), hiy

    return False, positions[-1], hiy


possible = []
traj_x, traj_y = -1, -1

# Minimum dy cannot go past the lowest target y in the first step
for dy in range(min_y, 180):  # Arbitrary end

    # dx cannot overshoot the target max_x in the first step
    for dx in range(max_x + 1):
        hit, (x, y), _ = hits_target(dx, dy)
        DEB("launched", (dx, dy), hit)

        if hit:
            traj_x, traj_y = dx, dy
            possible.append((dx, dy))
            DEB("Possble trajectory with", (dx, dy))

DEB(f"Highest dy possible is {traj_y}", (traj_x, traj_y))
_, _, p1 = hits_target(traj_x, traj_y)
p2 = len(possible)
DEB("possible:", possible)


print(f"p1={p1}")  # Is 15400, not 55, 3741, 7140 (too low)
print(f"p2={p2}")  # Is 5844, not 147, 2302 (too low)
