import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "1.in"
p1 = 0
p2 = 0

elves = []

calories = 0
for line in open(filename):
    if line.strip() == "":
        elves.append(calories)
        calories = 0
        continue
    calories += int(line.strip())

# Push last elf too
elves.append(calories)
p1 = max(elves)
p2 = sum(sorted(elves)[-3:])


print(f"p1={p1}")
print(f"p2={p2}")
