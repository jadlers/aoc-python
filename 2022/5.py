import sys
import re

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "5.in"
p1 = 0
p2 = 0


s1 = [[] for _ in range(11)]  # same index as in problem
s2 = []
setup = True
move_re = re.compile(r"^move (\d+) from (\d+) to (\d+)$")

for line in open(filename):
    if line == "\n":
        continue
    if setup:
        if line.startswith(" 1"):
            setup = False
            for s in s1:
                s.reverse()
            # print("setup done", s1)
            s2 = [c.copy() for c in s1]
            continue

        for (idx, ch) in enumerate(line):
            if (idx) % 4 == 1 and ch != " ":
                # stack same as in problem
                stack = (idx // 4) + 1
                s1[stack].append(ch)
        continue

    # Moving stacks
    matches = move_re.match(line)
    assert matches != None
    m, f, t = [int(x) for x in matches.groups()]

    # P1
    for _ in range(m):
        s1[t].append(s1[f].pop())

    # P2
    s2[t].extend(s2[f][-m:])
    s2[f] = s2[f][:-m]

p1 = "".join([c.pop() for c in s1[1:] if len(c) > 0])
p2 = "".join([c.pop() for c in s2[1:] if len(c) > 0])

print(f"p1={p1}")
print(f"p2={p2}")
