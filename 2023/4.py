import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "4.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

p1, p2 = 0, 0


for r, line in enumerate(X):
    # Parse out numbers with position
    winning, numbers = [
        [int(d) for d in nums.strip().split()] for nums in line.split(":")[1].split("|")
    ]

    wins = 0
    for w in winning:
        if w in numbers:
            wins += 1
    if wins > 0:
        p1 += 2 ** (wins - 1)


print(p1)
print(p2)
