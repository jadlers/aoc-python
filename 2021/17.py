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


# assert hits_target(7, 2)[0]
# assert hits_target(9, 0)[0]
# assert not hits_target(17, -4)[0]
# assert not hits_target(0, 0)[0]

traj_x, traj_y = -1, -1
old_max_dy = -1
max_dy = 0
# while max_dy != old_max_dy:
for sdy in range(180):  # Arbitrary end
    old_max_dy = max_dy
    was_lower = False
    dx, dy = 0, sdy  # max_dy + 1
    hit, (x, y), _ = hits_target(dx, dy)

    while not hit:
        if x > max_x:
            # DEB(f"Overshot, not possible with current dy={dy}")
            break

        if x <= max_x:
            dx += 1
            # DEB(x, min_x, f"increasing dx to {dx}")

        # Try again
        hit, (x, y), _ = hits_target(dx, dy)
        # DEB("launched", (dx, dy), hit)

    if hit:
        traj_x, traj_y = dx, dy
        max_dy = dy
        DEB("Possble trajectory with", (dx, dy))
    else:
        # DEB(f"Can't hit target with dy={dy}")
        # break
        pass

DEB(f"Highest dy possible is {traj_y}", (traj_x, traj_y))
_, _, p1 = hits_target(traj_x, traj_y)


print(f"p1={p1}")  # Is 15400, not 55, 3741, 7140 (too low)
print(f"p2={p2}")
