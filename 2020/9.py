import fileinput

lines = [int(x.strip()) for x in fileinput.input()]
p1 = 0
p2 = 0

# preamble = 5
preamble = 25


def valid(num, rge):
    for i in range(len(rge)):
        for j in range(i, len(rge)):
            if rge[i] + rge[j] == num:
                return True

    return False


for i in range(preamble, len(lines)):
    l = lines[i]
    rge = lines[i - preamble : i]
    ok = valid(l, rge)
    if not ok:
        p1 = l
        break

# Find contigous set
for i in range(len(lines)):
    beg = i
    # print(f"beg={beg} ({lines[i]})")
    s = 0
    while s < p1:
        s += lines[i]

        if s == p1 and lines[i] != p1:
            rge = lines[beg : i + 1]
            lo = min(rge)
            hi = max(rge)
            # 35321204 incorrect

            # print(beg, i)
            # print(lo, hi)
            p2 = lo + hi
        i += 1


print("p1:", p1)
print("p2:", p2)
