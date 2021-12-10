import sys
from collections import deque

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"

p1 = 0
p2 = []

match = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

points1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

points2 = {")": 1, "]": 2, "}": 3, ">": 4}


def find_corruption(line):
    q = deque()
    for idx, ch in enumerate(line):
        if ch in ["(", "[", "{", "<"]:  # Add opening symbol to queue
            q.append(ch)
        else:  # Match with last opening symbol
            l = q.pop()
            if l != match[ch]:
                # print(f'should match={l} got={ch} score={points1[ch]}')
                return idx, ch, q
    return -1, " ", q


assert find_corruption("([])")[0] == -1
assert find_corruption("{()()()}")[0] == -1
assert find_corruption("<([{}])>")[0] == -1
assert find_corruption("[<>({}){}[([])<>]]")[0] == -1


incomplete = []
for i, line in enumerate(open(filename)):
    line = line.strip()
    idx, ch, _ = find_corruption(line)
    # print(f"#{i+1:3d} {idx:3d}", ch, line)
    if idx != -1:
        p1 += points1[ch]
    else:
        incomplete.append(line)

for line in incomplete:
    _, _, q = find_corruption(line)
    q.reverse()
    score = 0
    for ch in q:
        score *= 5
        score += points2[match[ch]]
    # print(q, score)
    p2.append(score)

p2.sort()
p2 = p2[len(p2) // 2]


print(f"p1={p1}")  # NOT 333603 (too low)
print(f"p2={p2}")
