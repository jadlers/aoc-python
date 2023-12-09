import sys
from collections import defaultdict
from functools import cmp_to_key, partial
from typing import DefaultDict

filename = sys.argv[1] if len(sys.argv) > 1 else "7.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]
p1, p2 = 0, 0

O1 = "AKQJT98765432"
O2 = "AKQT98765432J"


def determine_type(vals):
    s = sorted(vals, reverse=True)
    if s[0] == 5:
        return 7
    elif s[0] == 4:
        return 6
    elif s[0] == 3 and s[1] == 2:
        return 5
    elif s[0] == 3:
        return 4
    elif s[0] == 2 and s[1] == 2:
        return 3
    elif s[0] == 2:
        return 2
    return 1


def determine_type2(groups: DefaultDict[str, int]):
    jokers = 0
    if "J" in groups:
        jokers = groups.pop("J")
    if jokers == 0:
        return determine_type(groups.values())
    elif jokers == 5:
        return 7
    s = sorted(groups.values(), reverse=True)
    if s[0] + jokers == 5:
        return 7
    elif s[0] + jokers == 4:
        return 6
    for j in range(jokers):
        # Only if 2 pairs of 2 and a joker, right?
        j1, j2 = jokers - j, j
        if s[0] + j1 == 3 and s[1] + j2 == 2:
            return 5
        elif s[0] + jokers == 3:
            return 4
        elif s[0] + j1 == 2 and s[1] + j2 == 2:
            return 3
    if s[0] + jokers == 2:
        return 2
    return 1


hb = {}
typed_hands = defaultdict(list[str])
typed_hands2 = defaultdict(list[str])
for i, line in enumerate(X):
    hand, bid = line.split()
    hb[hand] = int(bid)

    d = defaultdict(int)
    for ch in hand:
        d[ch] += 1

    hand_type = determine_type(d.values())
    typed_hands[hand_type].append(hand)

    hand_type2 = determine_type2(d)
    typed_hands2[hand_type2].append(hand)


def card_order(O, a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        ai = O.index(a[i])
        bi = O.index(b[i])
        if ai == bi:
            continue
        return bi - ai
    return 0


rank = 1
for t in sorted(typed_hands):
    ordered_hands = sorted(typed_hands[t], key=cmp_to_key(partial(card_order, O1)))
    for hand in ordered_hands:
        p1 += hb[hand] * rank
        rank += 1

rank = 1
for t in sorted(typed_hands2):
    ordered_hands = sorted(typed_hands2[t], key=cmp_to_key(partial(card_order, O2)))
    for hand in ordered_hands:
        p2 += hb[hand] * rank
        rank += 1


print(p1)
print(p2)
