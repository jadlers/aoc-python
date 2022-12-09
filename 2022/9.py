import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "9.in"
p1 = 0
p2 = 0


h = (0, 0)  # row, col
t = (0, 0)

DIRS = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
visited = set((0,0))

step = 0
for line in open(filename):
    dir, dist = line.strip().split()
    dist = int(dist)
    print(dir, dist)

    dr, dc = DIRS[dir]
    for _ in range(dist):
        step += 1
        h = (h[0] + dr, h[1] + dc)
        hr, hc = h

        tr, tc = t
        sr = hr - tr
        sc = hc - tc
        if abs(sr) > 1 or abs(sc) > 1:
            if sr > 1:
                t = (t[0] + 1, h[1])
            elif sr < -1:
                t = (t[0] - 1, h[1])
            elif sc > 1:
                t = (h[0], t[1] + 1)
            elif sc < -1:
                t = (h[0], t[1] - 1)

            visited.add(t)

            # print("move tail!", h, t, sr, sc)
        print("both moved:", h, t)

p1 = len(visited) # 13 for test
print(f"p1={p1}") # Not: 6080
print(f"p2={p2}")
