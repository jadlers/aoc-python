import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "11.in"

p1 = 0
p2 = 0

O = [[int(x) for x in y.strip()] for y in open(filename)]
R = len(O)
C = len(O[0])

DR = [-1, -1, -1, 0, 0, 1, 1, 1]
DC = [-1, 0, 1, -1, 1, -1, 0, 1]

for row in O:
    print(row)
print()


def flash(o, r, c):
    for d in range(8):
        rr = r + DR[d]
        cc = c + DC[d]

        if 0 <= rr < R and 0 <= cc < C:
            o[rr][cc] += 1
            if o[rr][cc] == 10:
                flash(o, rr, cc)


for _ in range(100):  # range 100
    flashed = [[False for _ in range(R)] for _ in range(C)]

    # Increase each octopus value
    for r in range(R):
        for c in range(C):
            O[r][c] += 1
            if O[r][c] == 10:
                flash(O, r, c)

    # Reset all with value >= 9 and reset
    for r in range(R):
        for c in range(C):
            if O[r][c] > 9:
                p1 += 1
                O[r][c] = 0

    for row in O:
        print(row)
    print()

# for line in open(filename):
#     line = line.strip()


print(f"p1={p1}")
print(f"p2={p2}")
