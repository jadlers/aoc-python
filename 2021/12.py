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
        add_edge(s, e, bidirectional=False)
    else:
        add_edge(s, e)


def included_twice(s, visited):
    """Returns True if state `s` is included twice in `visited`, False otherwise"""
    try:
        idx = visited.index(s)
        return visited[idx + 1] == s
    except (ValueError):
        return False  # Not included at all
    except (IndexError):
        return False  # Last in list i.e. exists once


def new_path(path, s):
    new = path.copy()
    new.append(s)
    return new


def step(paths, p2: bool):
    """Take one step from each path in `paths` and return the new paths"""
    done = []
    next = []
    for path in paths:
        visited = [x for x in path if x[0] in LOWER]  # only visit small caves once
        visited.sort()
        has_revisit = False
        for i, v in enumerate(visited):
            if i == 0:
                continue
            if visited[i - 1] == v:
                has_revisit = True
                break

        for n in M[path[-1]]:
            # Add any state as long as there is no state revisited
            if (p2 and not has_revisit) or (
                n not in visited
            ):  # Don't include revisits for p1
                new = new_path(path, n)
                if n == "end":
                    done.append(new)
                else:
                    next.append(new)

    return done, next


def run(p2):
    complete = []
    _, queue = step([["start"]], p2)
    while len(queue) > 0:
        done, queue = step(queue, p2)
        complete.extend(done)

    return len(complete)


p1 = run(p2=False)
p2 = run(p2=True)


print(f"p1={p1}")
print(f"p2={p2}")
