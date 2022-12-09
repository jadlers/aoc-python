import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "9.in"
p1 = 0
p2 = 0
print_it = False

X = [x.strip() for x in open(filename)]
DIRS = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}


def move(head, tail):
    """Return the tail given how head has moved."""
    hr, hc = head
    tr, tc = tail

    sr = hr - tr
    sc = hc - tc
    if abs(sr) > 1 and abs(sc) > 1:
        tail = (tail[0] + (sr//2), tail[1] + (sc//2))
    elif sr > 1:
        tail = (tail[0] + 1, hc)
    elif sr < -1:
        tail = (tail[0] - 1, hc)
    elif sc > 1:
        tail = (hr, tail[1] + 1)
    elif sc < -1:
        tail = (hr, tail[1] - 1)

    return head, tail


v1 = set()
v2 = set()

# Knots in rope
K: list[tuple[int, int]] = [(0, 0) for _ in range(10)]

for line in X:
    dir, dist = line.split()
    dist = int(dist)
    # print(dir, dist)

    dr, dc = DIRS[dir]
    for s in range(dist):
        # Move head according to instruction
        h = K[0]
        K[0] = (h[0] + dr, h[1] + dc)
        # print("head moved", K[0])

        # for every other knot in the rope
        for i in range(0, len(K) - 1):
            # print(i, i + 1)
            h = K[i]
            t = K[i + 1]

            h, t = move(h, t)
            K[i] = h
            K[i + 1] = t

            if i + 1 == 1:
                v1.add(t)
            if i + 1 == len(K) - 1:
                v2.add(t)

        # Do I print it? Comment out to print
        if print_it:
            M = {}
            for i, knot in enumerate(K):
                if knot in M:
                    continue
                M[knot] = str(i) if i > 0 else "H"

            for r in range(4, -1, -1):
                print("".join([M[(-r, c)] if (-r, c) in M else "." for c in range(6)]))
            print()


p1 = len(v1)  # 13 for test
p2 = len(v2)  # 36 for test, new input (1 original)
print(f"p1={p1}")
print(f"p2={p2}")
