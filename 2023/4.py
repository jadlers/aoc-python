import sys
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "4.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

p1, p2 = 0, 0


num_cards = defaultdict(int)
for i in range(len(X)):
    num_cards[i] = 1
card_points = defaultdict(int)


def wins(game, winning, numbers):
    if game in card_points:
        return card_points[game]
    wins = 0
    for w in winning:
        if w in numbers:
            wins += 1
    card_points[game] = 2 ** (wins - 1) if wins > 0 else 0
    return wins


for i, line in enumerate(X):
    winning, numbers = [
        [int(d) for d in nums.strip().split()] for nums in line.split(":")[1].split("|")
    ]

    w = wins(i, winning, numbers)
    for g in range(i + 1, i + 1 + w):
        if g > len(X):
            continue
        num_cards[g] += num_cards[i]

p1 = sum(card_points.values())
p2 = sum(num_cards.values())

print(p1)
print(p2)
