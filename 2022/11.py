import sys
from copy import deepcopy
from math import lcm

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "11.in"
p1 = 0
p2 = 0

X = [x.strip() for x in open(filename)]


def do_op(old, op, rhs):
    global MAX
    if rhs == "old":
        rhs = old

    rhs = int(rhs)
    assert op in ["*", "+"], op
    return old * rhs if op == "*" else old + rhs


M = []
m = {}
divs = set()
for i in range(0, len(X), 7):
    m = {}
    items = X[i + 1].split()
    items = [int(x.strip(",")) for x in items[2:]]
    m["items"] = items

    operation = X[i + 2].split()
    assert operation[3] == "old", operation
    op, num = operation[-2:]
    m["op"] = op
    m["num"] = num

    div = int(X[i + 3].split().pop())
    m["div"] = div
    divs.add(div)

    truthy = int(X[i + 4].split().pop())
    falsy = int(X[i + 5].split().pop())
    m["truthy"] = truthy
    m["falsy"] = falsy

    # print(X[i], m)
    M.append(m)

MAX = lcm(*divs)
# print("lcm:", MAX)

# Let's start the game
INIT = deepcopy(M)
throws = [0 for _ in range(len(M))]


def round(part):
    global M
    for m_idx, m in enumerate(M):
        items = m["items"].copy()
        throws[m_idx] += len(items)
        m["items"] = []
        for i in items:
            new_i = do_op(i, m["op"], m["num"])
            if part == 1:
                new_i = new_i // 3
            elif part == 2:
                new_i %= MAX
            if new_i % m["div"] == 0:
                # print(new_i, m["div"])
                M[m["truthy"]]["items"].append(new_i)
            else:
                M[m["falsy"]]["items"].append(new_i)


for part in [1, 2]:
    M = deepcopy(INIT)
    throws = [0 for _ in range(len(M))]
    for i in range(20 if part == 1 else 10000):
        round(part)

    m1, m2 = sorted(throws)[-2:]
    print(f"p{part}={m1*m2}")
