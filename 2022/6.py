import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "6.in"
p1 = 0
p2 = 0

X = [l for l in open(filename)]
line = X[0]

for i in range(4, len(line)):
    g1 = line[i-4:i]
    s1 = set(g1)
    if not p1 and len(s1) == 4:
        p1 = i
    if i < 14:
        continue

    g2 = line[i-14:i]
    s2 = set(g2)
    if not p2 and len(s2) == 14:
        p2 = i


    if p1 and p2:
        break

print(f"p1={p1}")
print(f"p2={p2}")
