import sys
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
    new = old * rhs if op == "*" else old + rhs
    new = new % MAX
    return new


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
print("lcm:", MAX)

# Let's start the game
throws = [0 for _ in range(len(M))]


def round():
    global M
    for m_idx, m in enumerate(M):
        items = m["items"].copy()
        throws[m_idx] += len(items)
        m["items"] = []
        for i in items:
            new_i = do_op(i, m["op"], m["num"])
            if new_i % m["div"] == 0:
                # print(new_i, m["div"])
                M[m["truthy"]]["items"].append(new_i)
            else:
                M[m["falsy"]]["items"].append(new_i)


for i in range(10000):
    round()

m1, m2 = sorted(throws)[-2:]
p2 = m1 * m2

print(f"p1={p1}")
print(f"p2={p2}")
