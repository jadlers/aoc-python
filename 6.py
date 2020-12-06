import fileinput

lines = [x.strip() for x in fileinput.input()]
lines.append("")

s = set()
groups = []
fline = True
for line in lines:
    if line == "":  # end of group
        groups.append(s.copy())
        s = set()
        fline = True

    else:
        if fline:  # First round
            fline = False
            for ch in line:
                s.add(ch)

        else:
            next = set()
            for ch in line:
                if ch in s:
                    next.add(ch)

            s = next.copy()

p1 = 0
for g in groups:
    p1 += len(g)


print(p1)
