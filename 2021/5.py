import sys
import re

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0


def draw_line(M, start, end):
    a, b = start
    x, y = end
    if b == y:  # Horizontal
        for i in range(min(a, x), max(a, x) + 1):
            # M[y][x]
            M[b][i] += 1
    elif a == x:  # Vertical
        for i in range(min(b, y), max(b, y) + 1):
            # M[y][x]
            M[i][a] += 1
    else:
        print("skip")


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


def part1():
    M = [[0 for _ in range(hix + 1)] for _ in range(hiy + 1)]
    for x in xs:
        draw_line(M, x[0], x[1])
    tot = 0
    for row in M:
        s = len(list(filter(lambda x: x > 1, row)))
        tot += s
        # print(s, row)
    return tot
    # return sum([sum(filter(lambda x: x>1, row)) for row in M])


def part2():
    pass


# NOT 6015
p1 = part1()
# p2 = part2(nums)

print(f"p1={p1}")
print(f"p2={p2}")
