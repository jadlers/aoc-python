import fileinput

lines = [x.strip() for x in fileinput.input()]
lines.append("")

s = set()
groups = []
for line in lines:
    if line == "":  # end of group
        groups.append(s.copy())
        s = set()

    for ch in line:
        s.add(ch)

p1 = 0
for g in groups:
    p1 += len(g)


print(p1)
