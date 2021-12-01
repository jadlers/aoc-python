import fileinput

groups = [x.split("\n") for x in open(0).read().strip().split("\n\n")]

p1 = 0
p2 = 0
s1 = set()
for group in groups:
    s1 = set(group[0])  # First in the group
    s2 = s1.copy()
    for other in group[1:]:
        s1 = s1 | set(other)
        s2 = s2 & set(other)

    p1 += len(s1)
    p2 += len(s2)

    # print(f"group: {group} => s1: {s1}")
    # print(f"group: {group} => s2: {s2}")

print("p1:", p1)
print("p2:", p2)
