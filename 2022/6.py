import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "6.in"
p1 = 0
p2 = 0

X = [l for l in open(filename)]
line = X[0]


def find_dup(chars: str) -> bool:
    """`find_dup` return `True` when there's a char in the string which occur
    more than once, `False` otherwise."""
    for idx, ch in enumerate(chars[:-1]):
        if ch in chars[idx + 1 :]:
            return True
    return False


for i in range(4, len(line)):
    if not p1:
        g1 = line[i - 4 : i]
        if not find_dup(g1):
            p1 = i
    if i < 14:
        continue
    elif not p2:
        g2 = line[i - 14 : i]
        if not find_dup(g2):
            p2 = i

    if p1 and p2:
        break

print(f"p1={p1}")
print(f"p2={p2}")
