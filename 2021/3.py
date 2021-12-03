import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

columns = {}
for line in open(filename):
    for (i, n) in enumerate(line.strip()):
        if i not in columns:
            columns[i] = []
        columns[i].append(n)


vals = {}
for i in columns:
    ones = columns[i].count('1')
    zero = columns[i].count('0')

    vals[i] = {
        "gam": "1" if ones > zero else "0",
        "eps": "1" if ones < zero else "0",
    }

gamma = "".join([vals[x]["gam"] for x in vals])
epsilon = "".join([vals[x]["eps"] for x in vals])

print(gamma, epsilon)

p1 = int(gamma, base=2) * int(epsilon, base=2)

print(f"p1={p1}")
print(f"p2={p2}")
