import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "4.in"
X = [x.strip() for x in open(filename)]
p1 = 0
p2 = 0


def pline(s, e):
    """Print a line where each char correspond to a section. The char is `"#"`
    when the Elves shall clean it and `" "` otherwise."""
    return "".join(["x" if s <= i + 1 <= e else " " for i in range(e)])


for line in X:
    [[a, b], [x, y]] = [[int(y) for y in x.split("-")] for x in line.strip().split(",")]

    # P1
    if a <= x and b >= y:
        p1 += 1
    elif x <= a and y >= b:
        p1 += 1

    # P2
    fst = set([c for c in range(a, b + 1)])
    snd = set([c for c in range(x, y + 1)])
    if len(fst & snd) > 0:
        p2 += 1


print(f"p1={p1}")
print(f"p2={p2}")
