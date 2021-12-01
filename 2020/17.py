import fileinput
import itertools
import re
import sys

ys = [x.strip() for x in fileinput.input()]

M = {}
for (y, xs) in enumerate(ys):
    for (x, ch) in enumerate(xs):
        M[f"{x}:{y}:0"] = ch


def surrounding_coords(x, y, z):
    diff = [-1, 0, 1]

    coords = []
    for dx in diff:
        x_ = x + dx
        for dy in diff:
            y_ = y + dy
            for dz in diff:
                z_ = z + dz
                if x_ == x and y_ == y and z_ == z:
                    continue
                coords.append((x_, y_, z_))

    return coords


def count_active(x, y, z):
    count = 0
    coords = surrounding_coords(x, y, z)
    for (x_, y_, z_) in coords:
        if M.get(f"{x_}:{y_}:{z_}", ".") == "#":
            count += 1

    return count


def step():
    C = {}
    for coord in M:
        x, y, z = [int(x) for x in re.findall("-?\d+", coord)]
        surrounding = surrounding_coords(x, y, z)
        for (x, y, z) in surrounding:
            if f"{x}:{y}:{z}" not in C:
                C[f"{x}:{y}:{z}"] = count_active(x, y, z)

    for coord in C:
        x, y, z = [int(x) for x in re.findall("-?\d+", coord)]
        active = True if M.get(f"{x}:{y}:{z}", ".") == "#" else False
        surr = C.get(f"{x}:{y}:{z}", 0)

        # print(f"{x}:{y}:{z} active={active} surr={surr}")

        if active and surr not in [2, 3]:
            M[f"{x}:{y}:{z}"] = "."
            # print(f"{x}:{y}:{z} inactivating, had {surr} active neighbors")
        elif not active and surr == 3:
            M[f"{x}:{y}:{z}"] = "#"
            # print(f"{x}:{y}:{z} activating, had {surr} active neighbors")


def count_all():
    count = 0
    for k in M:
        if M[k] == "#":
            count += 1

    return count


# step()
for i in range(6):
    # print(f"Step {i+1}")
    step()

print(count_all())
