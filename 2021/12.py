import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "11.in"

p1 = 0
p2 = 0

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = UPPER.lower()

M = {}


def add_edge(a, b, bidirectional=True):
    global M
    if a not in M:
        M[a] = [b]
    else:
        M[a].append(b)
    if not bidirectional:
        return

    if b not in M:
        M[b] = [a]
    else:
        M[b].append(a)



# Parse input
for line in open(filename):
    s, e = line.strip().split("-")
    if s == "start" or e == "end":
        add_edge(s,e,bidirectional=False)
    else:
        add_edge(s,e)

# Could remove all entries where a small cave only have connection to **one**
# small cave

def step(paths):
    """Take one step from each path in `paths` and return the new paths"""
    done = []
    next = []
    for path in paths:
        visited = [x for x in path if x[0] in LOWER] # only visit small caves once
        # print('visited:', visited)

        for n in M[path[-1]]:
            if n not in visited:
                new = path.copy()
                new.append(n)
                if n == 'end':
                    done.append(new)
                else:
                    next.append(new)
            # print('can go to', n)

    # print(done, next)
    return done, next


complete = []
_, queue = step([['start']])
last_len = -1
# for _ in range(10):
# while last_len < len(n):
while len(queue) > 0:
    done, queue = step(queue)
    complete.extend(done)

# print(queue)
# print(len(complete), complete)
p1 = len(complete)



print(f"p1={p1}")
print(f"p2={p2}")
