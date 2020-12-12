import fileinput

lines = [(x[0], int(x[1:])) for x in fileinput.input()]

x = 0
y = 0

facing = 90

n = 0
e = 0
w = 0
s = 0

p1 = 0
p2 = 0
n = 0
for (d, l) in lines:
    # n += 1
    # if n < 20:
    #     print(f"{x}\t{y}\t{dir_}\t({d} {l})")

    if d == "N" or d == "F" and facing == 0:
        y += l
        n += l
    elif d == "E" or d == "F" and facing == 90:
        x += l
        e += l
    elif d == "S" or d == "F" and facing == 180:
        y -= l
        s += l
    elif d == "W" or d == "F" and facing == 270:
        x -= l
        w += l
    elif d == "R":
        # print(f"pre  dir={dir}, R{l}")
        facing += l
        facing %= 360
        assert facing in [0, 90, 180, 270]
        # print(f"post dir={dir}, R{l}")
        # print()
    elif d == "L":
        # print(f"pre  dir={dir}, L{l}")
        facing -= l
        facing %= 360
        assert facing in [0, 90, 180, 270]
    else:
        assert False
        print("GOT HERE")
        # print(f"post dir={dir}, L{l}")
        # print()
    # print(f"{x}\t{y}\t{dir_}\t({d} {l})")
    # print(f"{x}\t{y}\t{facing}\t({d} {l})")

print(f"n={n} e={e} s={s} w={w}")
print(abs(e - w))
print(abs(n - s))
print(x, y)
# 7136 not correct, 6864 not correct
print("p1:", abs(x) + abs(y))
print("p2:", p2)
