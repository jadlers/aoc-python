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
print(R, C)

least_cost = [[1e9 for _ in range(C)] for _ in range(R)]
least_cost[0][0] = 0  # rows[0][0]

# Idea: From the start position (0,0) take all possible steps and store the
# lowest possible score to get there.
Q = set()
Q.add((0, 0))

while Q:
    r, c = Q.pop()
    print("current", (r, c))
    for i in range(2):
        rr = r + DR[i]
        cc = c + DC[i]
        if 0 <= rr < R and 0 <= cc < C:
            Q.add((rr, cc))
            this_cost = least_cost[r][c] + rows[rr][cc]
            if this_cost < least_cost[rr][cc]:
                least_cost[rr][cc] = this_cost


print(rows)
print(least_cost)
p1 = least_cost[-1][-1]


print(f"p1={p1}")
print(f"p2={p2}")
