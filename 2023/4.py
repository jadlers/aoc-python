import sys
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "4.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]


# Number of cards at key, note not using game number but line number.
# line = game - 1.
num_cards: defaultdict[int, int] = defaultdict(int)
for i in range(len(X)):
    num_cards[i] = 1
# Number of wins. Keyed just like `num_cards`
card_wins: defaultdict[int, int] = defaultdict(int)


def wins(game: int, winning: list[int], numbers: list[int]):
    """
    Calculates the number of wins in a game. Also store the scoring for the
    game in `num_cards`. 1p for the first win which is doubled for every other
    win in the row.
    """
    wins = 0
    for w in winning:
        if w in numbers:
            wins += 1
    card_wins[game] = 2 ** (wins - 1) if wins > 0 else 0
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

p1 = sum(card_wins.values())
p2 = sum(num_cards.values())

print(p1)
print(p2)
