import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "1.in"
p1 = 0
p2 = 0

candidate = 0
for line in open(filename):
    if line.strip() == "":
        p1 = max(p1, candidate)
        candidate = 0
        continue
    candidate += int(line.strip())


print(f"p1={p1}")
print(f"p2={p2}")
