import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "4.in"
X = [x.strip() for x in open(filename)]
T = ["1-1,1-1"]
p1 = 0
p2 = 0


def pline(s, e):
    return "".join(["x" if s <= i + 1 <= e else " " for i in range(e)])


# for line in open(filename):
for line in X:
    [[a, b], [x, y]] = [[int(y) for y in x.split("-")] for x in line.strip().split(",")]

    # print("range", max(b,y)-min(a,x))
    # print("width", max(b,y))
    # print(a, b, x, y)
    if a <= x and b >= y:
        # print(a, b, x, y)
        p1 += 1
    elif x <= a and y >= b:
        # print(a, b, x, y)
        p1 += 1
    else:
        pass
        # print(a,b,x,y)
        # print("1", pline(a,b))
        # print("2", pline(x,y))
        # print('nope')
    # print()

    # P2
    fst = set([c for c in range(a, b + 1)])
    snd = set([c for c in range(x, y + 1)])
    if len(fst & snd) > 0:
        p2 += 1


print(f"p1={p1}")  # 512
print(f"p2={p2}")  #
