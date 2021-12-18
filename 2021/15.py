import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "15.in"

p1 = 0
p2 = 0

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

rows = []
for line in open(filename):
    rows.append([int(x) for x in line.strip()])

R = len(rows)
C = len(rows[0])


def cost_to(costs, r, c):
    if r < 0 or c < 0:
        return int(1e9)
    return costs[r][c]


def min_dist(dists, R, C):
    """Return ((r,c), v) for item with lowest v in `dists`"""
    return sorted(dists.items(), key=lambda item: item[1]).pop(0)
    s = dists.items()
    s = list(filter(lambda x: x[1] < float("inf"), s))

    t = []
    for (r, c), v in s:
        if v == float("inf"):
            continue
        # Add heuristic of manhattan dist to goal, since each step costs at least one
        t.append(((r, c), v + R - 1 - r + C - 1 - c))

    t.sort(key=lambda item: item[1])
    # print(t)

    return t[0]
    # min_coord = (0, 0)
    # min_val = None
    # for c, v in dists.items():
    #     if min_val == None:
    #         min_coord = c
    #         min_val = v
    #     elif v < min_val:
    #         min_coord = c
    #         min_val = v

    # return min_coord


def calculate_least_cost(rows):
    R = len(rows)
    C = len(rows[0])
    goal = (R - 1, C - 1)
    assert R == C

    visited = {}
    Q = {}
    for r in range(R):
        for c in range(C):
            Q[(r, c)] = float("inf")
    Q[(0, 0)] = 0
    # least_cost = [[float('inf') for _ in range(C)] for _ in range(R)]
    # least_cost[0][0] = 0

    # IDEA: Is the problem that an optimal route won't always go right/down.
    # Will it actually at some point go up/left?
    # IDEA: Do Dijkstra's algorithm!
    # IDEA: Update to be A* by adding manhattan distance to goal when finding
    # min
    # for _ in range(10):
    while Q:
        if len(Q) % 1000 == 0:
            print(len(Q))

        (r, c), _ = min_dist(Q, R, C)
        cur_dist = Q.pop((r, c))

        # print("at", (r, c), "dist", cur_dist)
        for i in range(4):
            rr = r + DR[i]
            cc = c + DC[i]

            if not (0 <= rr < R and 0 <= cc < C):
                continue
            if (rr, cc) not in Q:
                continue

            # If (rr,cc) not visited and the distance to (r,c) + cost of going
            # to (rr,cc) is less that currently stored distance to (rr,cc) then
            # update the previous value
            alt = cur_dist + rows[rr][cc]
            if alt < Q[(rr, cc)]:
                Q[(rr, cc)] = alt
                if (rr, cc) == goal:
                    print("FOUND GOAL", alt)
                    return alt

        # Move current to visited
        # print('visited', (r,c), cur_dist)
        visited[(r, c)] = cur_dist

    # print(visited)
    # for i in range(1, R + C):  # Move in diagonals
    #     for r in range(i + 1):
    #         c = i - r
    #         if r >= R or c >= C:
    #             continue

    #         ar, ac = r - 1, c  # Above
    #         lr, lc = r, c - 1  # Left

    #         above_cost = cost_to(least_cost, ar, ac)
    #         left_cost = cost_to(least_cost, lr, lc)
    #         least = above_cost if above_cost < left_cost else left_cost
    #         least_cost[r][c] = least + rows[r][c]

    # print((r, c), "above", (ar, ac), above_cost, "left:", (lr, lc), left_cost)
    # print('least', least)

    return visited[(R - 1, C - 1)] if (R - 1, C - 1) in visited else -1
    # return least_cost[-1][-1]


p1 = calculate_least_cost(rows)


## Part 2
B = []
for tr in range(5):  # Tile row
    tile = [[] for _ in range(R)]
    for tc in range(5):  # Tile col
        for r, row in enumerate(rows):
            c = tr + tc
            ncol = [x + c if x + c < 10 else x + c - 9 for x in row]
            tile[r].extend(ncol)
    for row in tile:
        B.append(row)

p2 = calculate_least_cost(B)

print(f"p1={p1}")
print(f"p2={p2}")  # Not 2973 (too high)
