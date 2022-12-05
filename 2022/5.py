import sys
import re

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "5.in"
# X = [x.strip() for x in open(filename)]
p1 = 0
p2 = 0


stacks = [[] for _ in range(11)]  # same index as problem
setup = True
move_re = re.compile(r"^move (\d+) from (\d+) to (\d+)$")

for line in open(filename):
    if line == "\n":
        continue
    if setup:
        if line.startswith(" 1"):  # == "\n":
            setup = False
            for s in stacks:
                s.reverse()
            print("setup done", stacks)
            continue

        # print(line)
        for (idx, ch) in enumerate(line):
            if (idx) % 4 == 1 and ch != " ":
                comp = (idx // 4) + 1  # comp as in problem
                stacks[comp].append(ch)
        continue

    # Moving stacks
    matches = move_re.match(line)
    if not matches:
        print(line)
        continue
    # assert matches != None
    m, f, t = [int(x) for x in matches.groups()]
    # print(m, f, t)
    # print("move", stacks[f][-m:])
    # for _ in range(m):
    #     stacks[t].append(stacks[f].pop())
    stacks[t].extend(stacks[f][-m:])
    stacks[f] = stacks[f][:-m]
    # print(stacks[1:4])

p1 = "".join([c.pop() for c in stacks[1:] if len(c) > 0])

print(f"p1={p1}")
print(f"p2={p2}")
