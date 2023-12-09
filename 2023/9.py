import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "9.in"
data = open(filename).read().strip()
X = [[int(y) for y in x.strip().split()] for x in data.split("\n")]

p1, p2 = 0, 0


def find(hist: list[int], p1=True):
    # Base case
    if all([True if x == 0 else False for x in hist]):
        return 0

    assert len(hist) > 1, f"too short {hist}"
    next = [hist[i + 1] - hist[i] for i in range(len(hist) - 1)]

    if p1:
        last = hist[len(hist) - 1] + find(next)
        hist.append(last)
        return hist[len(hist) - 1]

    first = hist[0] - find(next, p1)
    hist.insert(0, first)
    return hist[0]


for i, history in enumerate(X):
    p1 += find(history)

for i, history in enumerate(X):
    p2 += find(history, p1=False)


print(p1)
print(p2)
