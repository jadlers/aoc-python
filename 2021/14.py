import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "14.in"

p1 = 0
p2 = 0

letters = set()
polymer = ""
R = {}

for line in open(filename):
    if polymer == "":
        polymer = [ch for ch in line.strip()]
        continue
    if not line.strip():
        continue

    # print(line)
    i, o = line.strip().split("->")
    (a,b) = [ch for ch in i.strip()]
    R[(a,b)] = o.strip()
    letters.add(a)
    letters.add(b)
    letters.add(o.strip())

def step(pol, R):
    new_pol = []
    for i in range(1, len(pol)):
        a, b = pol[i-1], pol[i]
        if (a,b) in R:
            new_pol.extend([a,R[(a,b)]]) # b added as a in next step
        else:
            new_pol.append(a)
    new_pol.append(pol[-1])

    return "".join(new_pol)

for i in range(10):
    polymer = step(polymer, R)
    # print(i+1, len(polymer))


occ = []
for ch in letters:
    # occurances[ch] = polymer.count(ch)
    occ.append(polymer.count(ch))

# occ = occurances.values()
occ.sort()
p1 = occ[-1]-occ[0]

print(f"p1={p1}")
print(f"p2={p2}")
