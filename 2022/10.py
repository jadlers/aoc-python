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


cycles = 0
pos = 1
ss = []
for parts in X:
    cmd = parts[0]
    # print(cmd, parts)
    if cmd == "noop":
        cycles += M[cmd]
        inc_ss(ss, cycles, pos)
    elif cmd == "addx":
        for _ in range(M[cmd]):
            cycles += 1
            inc_ss(ss, cycles, pos)
        pos += int(parts[1])

p1 = sum(ss)
print(f"p1={p1}")
print(f"p2={p2}")
