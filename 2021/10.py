import sys
from collections import deque

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"

p1 = 0
p2 = 0

match = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}

# STUPID ME SWAPPED ']' and '}' in scoring...
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def find_corruption(line):
    q = deque()
    for idx, ch in enumerate(line):
        if ch in ["(", "[", "{", "<"]:  # Add opening symbol to queue
            q.append(ch)
        else:  # Match with last opening symbol
            l = q.pop()
            if l != match[ch]:
                # print(f'{line} should match={l} got={ch}')
                print(f"should got={ch} score={points[ch]}")
                return idx, ch
    # if len(q) != 0: print('unmatched', q)
    if len(q) != 0:
        print("incomplete")
    return -1, " "


assert find_corruption("([])")[0] == -1
assert find_corruption("{()()()}")[0] == -1
assert find_corruption("<([{}])>")[0] == -1
assert find_corruption("[<>({}){}[([])<>]]")[0] == -1
# assert find_corruption("<([]){()}[{}])") == (13, ')')


errs = {}
for i, line in enumerate(open(filename)):
    line = line.strip()
    idx, ch = find_corruption(line)
    # print(f"#{i+1:3d} {idx:3d}", ch, line)
    if idx != -1:
        if ch not in errs:
            errs[ch] = 1
        else:
            errs[ch] += 1
        p1 += points[ch]

print("alt p1:", sum([points[ch] * n for ch, n in errs.items()]), errs)


print(f"p1={p1}")  # NOT 333603 (too low)
print(f"p2={p2}")
