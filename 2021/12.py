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

def included_twice(s, visited):
    """Returns True if state `s` is included twice in `visited`, False otherwise"""
    try:
        idx = visited.index(s)
        return visited[idx+1] == s
    except(ValueError):
        return False # Not included at all
    except(IndexError):
        return False # Last in list i.e. exists once


def step(paths):
    """Take one step from each path in `paths` and return the new paths"""
    done = []
    next = []
    for path in paths:
        visited = [x for x in path if x[0] in LOWER] # only visit small caves once
        visited.sort()
        has_revisit = False
        for i,v in enumerate(visited):
            if i == 0: continue
            if visited[i-1] == v:
                has_revisit = True
                break

        # print(path, has_revisit, visited)

        for n in M[path[-1]]:
            # Add any state as long as there is no state revisited
            if not has_revisit:
                # print('can go to', n)
                new = path.copy()
                new.append(n)
                if n == 'end':
                    done.append(new)
                else:
                    next.append(new)
            elif n not in visited:
                new = path.copy()
                new.append(n)
                if n == 'end':
                    done.append(new)
                else:
                    next.append(new)

    return done, next


complete = []
_, queue = step([['start']])
last_len = -1
# for _ in range(10):
# while last_len < len(n):
while len(queue) > 0:
    done, queue = step(queue)
    # print(len(done[0]), 'completed', done)
    complete.extend(done)

# print(queue)
# print(len(complete), complete)
p1 = len(complete)



print(f"p1={p1}")
print(f"p2={p2}")
