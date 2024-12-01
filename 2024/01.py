import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "8.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

p1, p2 = 0, 0

l1, l2 = [], []
for line in X:
    a, b = [int(y) for y in line.split()]
    l1.append(a)
    l2.append(b)


l1 = sorted(l1)
l2 = sorted(l2)


for i in range(len(l1)):
    p1 += abs(l1[i] - l2[i])


print(p1)

seen = {}
for x in l1:
    seen[x] = 0

for x in l2:
    if x not in seen:
        continue
    seen[x] += 1

p2 = 0
for x in l1:
    if x not in seen:
        continue
    a = x * seen[x]
    p2 += a

# 262113297 too high
print(p2)
