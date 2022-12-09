import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "9.in"
p1 = 0
p2 = 0


X = [x.strip() for x in open(filename)]
DIRS = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}


def move(head, tail):
    """Return the tail given how head has moved."""
    hr, hc = head
    tr, tc = tail

    sr = hr - tr
    sc = hc - tc
    if sr > 1:
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
    for _ in range(dist):
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

            # print(f"both moved ({i}, {i+1}):", h, t)

p1 = len(v1)  # 13 for test
p2 = len(v2)
print(f"p1={p1}")  # Not: 6080
print(f"p2={p2}")  # Not: 2504
