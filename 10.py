import fileinput

xs = [int(x.strip()) for x in fileinput.input()]
p2 = 0
xs.sort()
ACCEPT = max(xs) + 3
xs.append(ACCEPT)

j3 = 0
j1 = 0
q = [0]  # Starting voltage
while len(q):
    e = q.pop(0)
    if e + 1 in xs:
        q.append(e + 1)
        j1 += 1
    elif e + 3 in xs:
        j3 += 1
        q.append(e + 3)

p1 = j1 * j3
print("p1:", p1)

paths = [0] * (ACCEPT + 1)
paths[0] = 1
for (_, x) in enumerate(xs):
    sum_ = paths[x - 3] + paths[x - 2] + paths[x - 1]
    paths[x] = sum_

print("p2:", paths[ACCEPT])
