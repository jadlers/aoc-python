import fileinput
from math import floor

p1 = 0
p2 = 0

xs = [int(x) for x in fileinput.input()]
print(xs[:3])
for x in xs:
    add = floor(x / 3) - 2
    p1 += add

    while add > 0:
        p2 += add
        add = floor(add / 3) - 2


print(p1)
print(p2)
