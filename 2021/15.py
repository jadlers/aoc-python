import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "15.in"

p1 = 0
p2 = 0

DR = [0, 1]
DC = [1, 0]

rows = []
for line in open(filename):
    rows.append([int(x) for x in line.strip()])

R = len(rows)
C = len(rows[0])


def cost_to(costs, r, c):
    if r < 0 or c < 0:
        return int(1e9)
    return costs[r][c]


def calculate_least_cost(rows):
    R = len(rows)
    C = len(rows[0])
    assert R == C

    least_cost = [[1e9 for _ in range(C)] for _ in range(R)]
    least_cost[0][0] = 0

    # IDEA: Is the problem that an optimal route won't always go right/down.
    # Will it actually at some point go up/left?
    for i in range(1, R + C):  # Move in diagonals
        for r in range(i + 1):
            c = i - r
            if r >= R or c >= C:
                continue

            ar, ac = r - 1, c  # Above
            lr, lc = r, c - 1  # Left

            above_cost = cost_to(least_cost, ar, ac)
            left_cost = cost_to(least_cost, lr, lc)
            least = above_cost if above_cost < left_cost else left_cost
            least_cost[r][c] = least + rows[r][c]

            # print((r, c), "above", (ar, ac), above_cost, "left:", (lr, lc), left_cost)
            # print('least', least)

    return least_cost[-1][-1]


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
