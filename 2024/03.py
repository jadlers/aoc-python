import re
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "03.in"
data = open(filename).read().strip()

p1, p2 = 0, 0

v2 = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")
on = True
for m in v2.findall(data):
    if m == "do()":
        on = True
    elif m == "don't()":
        on = False
    else:
        m = m[4:-1]  # Remove "mul(" and ")"
        x, y = map(int, m.split(","))
        p1 += x * y
        p2 = p2 + x * y if on else p2


print(p1)
print(p2)
