import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "02.in"
data = open(filename).read().strip()
lines = [x.strip() for x in data.split("\n")]

p1, p2 = 0, 0


def safe(line) -> bool:
    asc = True
    for i in range(len(line) - 1):
        delta = line[i + 1] - line[i]
        if i == 0:
            asc = delta > 0

        if abs(delta) > 3 or delta == 0:
            return False
        elif delta < 0 and asc:
            return False
        elif delta > 0 and not asc:
            return False

    return True


s1, s2 = 0, 0

for line in lines:
    line = [int(x) for x in line.split()]

    if safe(line):
        p1 += 1
        p2 += 1
        continue

    # Test by removing a single level at a time
    s = False
    for i in range(len(line)):
        l = line.copy()
        del l[i]
        if safe(l):
            p2 += 1
            s = True
            break


print(p1)
print(p2)
