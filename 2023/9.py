import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "9.in"
data = open(filename).read().strip()
X = [[int(y) for y in x.strip().split()] for x in data.split("\n")]

p1, p2 = 0, 0


def find(hist: list[int]):
    # Base case
    if all([True if x == 0 else False for x in hist]):
        return 0

    assert len(hist) > 1, f"too short {hist}"
    next = []
    for i in range(len(hist) - 1):
        diff = hist[i + 1] - hist[i]
        next.append(diff)

    last = hist[len(hist) - 1] + find(next)
    hist.append(last)
    return hist[len(hist) - 1]


for i, history in enumerate(X):
    p1 += find(history)


print(p1)
print(p2)
