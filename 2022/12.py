import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "12.in"
p1 = 0
p2 = 0


# Get the map
X = [x.strip() for x in open(filename)]
M = [[ord(c) - ord("a") for c in r] for r in X]
S = None
E = None
# Find start and goal
for r, row in enumerate(M):
    for c, val in enumerate(row):
        if val == -14:
            S = (r, c)
            M[r][c] = 0
        elif val == -28:
            E = (r, c)
            M[r][c] = ord("z") - ord("a")

HEIGHT = len(M)
WIDTH = len(M[0])
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def valid_steps(r, c):
    global M
    height = M[r][c]
    valid = []
    for dr, dc in DIR:
        rr = r + dr
        cc = c + dc
        if (0 <= rr < HEIGHT) and (0 <= cc < WIDTH):
            # print("check", (rr,cc), height, M[rr][cc])
            if M[rr][cc] <= height + 1:
                valid.append((rr, cc))
    return valid


dist_to = {S: 0}  # defaultdict? (r,c) -> dist
visited = set()  # of coords (r,c)
q = [S]

print(S, E)
for row in M:
    print(row)


def step():
    global q
    global dist_to
    global visited

    q.sort(key=lambda a: dist_to.get(a, 1e9), reverse=True)
    # print("queue  ", q)
    # print("dist_to", [dist_to[el] for el in q])
    # print("visited", visited)
    cur = q.pop()
    assert cur != None
    visited.add(cur)
    locations = valid_steps(cur[0], cur[1])
    for loc in locations:
        if loc not in visited and loc not in q:
            # print("add q", loc)
            if loc in dist_to and dist_to[loc] < dist_to[cur]:
                print("Detour")
            q.append(loc)
            dist_to[loc] = dist_to[cur] + 1

            if loc == E:
                return dist_to[loc]


def dist_map(distances):
    height_map = [
        [distances[(r, c)] if (r, c) in distances else "-" for c in range(WIDTH)]
        for r in range(HEIGHT)
    ]
    for row in height_map:
        print(row)


while True:
    found = step()
    if found:
        # print(dist_to)
        p1 = found
        dist_map(dist_to)
        break

print(f"p1={p1}")
print(f"p2={p2}")
