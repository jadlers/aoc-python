import sys
import re

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0


def draw_line(M, start, end, diagonal=False):
    a, b = start
    x, y = end
    if b == y:  # Horizontal
        for i in range(min(a, x), max(a, x) + 1):
            M[b][i] += 1  # M[y][x]
    elif a == x:  # Vertical
        for i in range(min(b, y), max(b, y) + 1):
            M[i][a] += 1  # M[y][x]

    elif diagonal:
        hor = None
        if a < x:
            hor = list(range(a, x + 1))
        else:
            hor = list(reversed(range(x, a + 1)))

        ver = None
        if b < y:
            ver = list(range(b, y + 1))
        else:
            ver = list(reversed(range(y, b + 1)))

        assert len(hor) == len(ver)
        for i in range(len(hor)):
            M[ver[i]][hor[i]] += 1

    else:
        # print("skip", a,b,x,y)
        pass


hix = None
hiy = None

xs = []
for line in open(filename):
    a, b, x, y = [int(x) for x in re.findall("\d+", line)]
    if hix is None or a > hix:
        hix = a
    elif hix is None or b > hix:
        hix = b
    if hiy is None or b > hiy:
        hiy = b
    elif hiy is None or y > hiy:
        hiy = y
    xs.append([(a, b), (x, y)])

# print(hix, hiy, xs)
# print(M)


def solve(diag=False):
    M = [[0 for _ in range(hix + 1)] for _ in range(hiy + 1)]
    for x in xs:
        draw_line(M, x[0], x[1], diag)
    tot = 0
    for row in M:
        s = len(list(filter(lambda x: x > 1, row)))
        tot += s
        # print(s, row)
    return tot


p1 = solve()  # NOT 6015
p2 = solve(diag=True)

print(f"p1={p1}")
print(f"p2={p2}")
