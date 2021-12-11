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


def show():
    global O
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


def has_val(O):
    for r in O:
        for c in r:
            if c > 0:
                return True
    return False


while has_val(O):
    # Increase each octopus value
    for r in range(R):
        for c in range(C):
            O[r][c] += 1
            if O[r][c] == 10:
                flash(O, r, c)

    # Reset all with value > 9
    for r in range(R):
        for c in range(C):
            if O[r][c] > 9:
                if p2 < 100:
                    p1 += 1
                O[r][c] = 0

    p2 += 1


print(f"p1={p1}")
print(f"p2={p2}")
