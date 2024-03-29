import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "8.in"
p1 = 0
p2 = 0

M = [[int(y) for y in x.strip()] for x in open(filename)]
height = len(M)
width = len(M[0])

dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def visible(r, c, val):
    # print(r, c, val)
    for dr, dc in dirs:
        # print(dr, dc)
        r_, c_ = r, c
        while True:
            r_ += dr
            c_ += dc
            if not (0 <= r_ < height) or not (0 <= c_ < width):
                return True
            if M[r_][c_] >= val:
                break
    return False


def distances(r, c, val):
    seen = [0, 0, 0, 0]
    for i, dir in enumerate(dirs):
        dr, dc = dir
        r_, c_ = r, c

        while (0 <= r_+dr < height) and (0 <= c_+dc < width):
            r_ += dr
            c_ += dc
            if M[r_][c_] <= val:
                seen[i] += 1
            elif M[r_][c_] == val:
                seen[i] += 1
                break
            else:
                break

    print((r,c), seen)
    res = 1
    for d in seen:
        res *= d
    return res


for r, row in enumerate(M):
    print(r, row)
print()

n = 0
candidates = []
for r, row in enumerate(M):
    for c, num in enumerate(row):
        if r == 0 or r == height - 1:
            p1 += 1
            continue
        elif c == 0 or c == width - 1:
            p1 += 1
            continue

        n += 1
        if visible(r, c, num):
            print(num, r, c)
            p1 += 1

        candidates.append(distances(r,c,num))

p2 = max(candidates)


assert n == (width * height) - (width * 2) - (height * 2) + 4
print(f"p1={p1}")
print(f"p2={p2}")
