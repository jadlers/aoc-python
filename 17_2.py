import fileinput
import itertools
import re
import sys

ys = [x.strip() for x in fileinput.input()]

M = {}
for (y, xs) in enumerate(ys):
    for (x, ch) in enumerate(xs):
        M[f"{x}:{y}:0:0"] = ch


def surrounding_coords(x, y, z, w):
    diff = [-1, 0, 1]

    coords = []
    for dx in diff:
        x_ = x + dx
        for dy in diff:
            y_ = y + dy
            for dz in diff:
                z_ = z + dz
                for dw in diff:
                    w_ = w + dw

                    if x_ == x and y_ == y and z_ == z and w_ == w:
                        continue
                    coords.append((x_, y_, z_, w_))

    return coords


def count_active(x, y, z, w):
    count = 0
    coords = surrounding_coords(x, y, z, w)
    for (x_, y_, z_, w_) in coords:
        if M.get(f"{x_}:{y_}:{z_}:{w_}", ".") == "#":
            count += 1

    return count


def step():
    C = {}
    for coord in M:
        x, y, z, w = [int(x) for x in re.findall("-?\d+", coord)]
        surrounding = surrounding_coords(x, y, z, w)
        for (x, y, z, w) in surrounding:
            if f"{x}:{y}:{z}:{w}" not in C:
                C[f"{x}:{y}:{z}:{w}"] = count_active(x, y, z, w)

    for coord in C:
        x, y, z, w = [int(x) for x in re.findall("-?\d+", coord)]
        active = True if M.get(f"{x}:{y}:{z}:{w}", ".") == "#" else False
        surr = C.get(f"{x}:{y}:{z}:{w}", 0)

        # print(f"{x}:{y}:{z} active={active} surr={surr}")

        if active and surr not in [2, 3]:
            M[f"{x}:{y}:{z}:{w}"] = "."
            # print(f"{x}:{y}:{z} inactivating, had {surr} active neighbors")
        elif not active and surr == 3:
            M[f"{x}:{y}:{z}:{w}"] = "#"
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
