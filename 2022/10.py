import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "10.in"
p1 = 0
p2 = 0

X = [x.strip().split() for x in open(filename)]
M = {"noop": 1, "addx": 2}


def inc_ss(strengths, cyc, x):
    """add signal strength (cycle * x) if on cycle 20 or every 40th cycle after
    that. I.e., 60, 100, 140."""

    if cyc > 20 and ((cyc + 20) % 40) == 0:
        # print(cyc, x, cyc * x)
        strengths.append(cyc * x)
        return
    elif cyc == 20:
        # print(cyc, x, cyc * x)
        strengths.append(cyc * x)
        return


def screen(crt):
    for row in crt:
        print("".join(row))


def draw(crt, cycle, pos):
    cycle -= 1  # for index in crt to be correct
    row = cycle // 40
    col = cycle % 40
    line = crt[row]
    sprite = [pos - 1, pos, pos + 1]

    # print(row, col, sprite, cycle in sprite)
    if col in sprite:
        line[col] = "x"

    return row, line


cycles = 0
pos = 1
ss = []
crt = [["." for _ in range(40)] for _ in range(6)]


for parts in X:
    cmd = parts[0]
    # print(cmd, parts)
    if cmd == "noop":
        cycles += M[cmd]
        inc_ss(ss, cycles, pos)
        r, line = draw(crt, cycles, pos)
        crt[r] = line
    elif cmd == "addx":
        for _ in range(M[cmd]):
            cycles += 1
            r, line = draw(crt, cycles, pos)
            crt[r] = line
            inc_ss(ss, cycles, pos)
        pos += int(parts[1])
        # print("new pos", pos)


p1 = sum(ss)
print(f"p1={p1}")
print("\np2:") # PAPKFKEJ
screen(crt)
