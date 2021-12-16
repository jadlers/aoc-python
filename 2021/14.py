import sys
from collections import defaultdict

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "14.in"

p1 = 0
p2 = 0

letters = set()
polymer = ""
R = {}


for line in open(filename):
    if polymer == "":
        polymer = [ch for ch in line.strip()]
        continue
    if not line.strip():
        continue

    i, o = line.strip().split("->")
    (a, b) = [ch for ch in i.strip()]
    R[(a, b)] = o.strip()


def ans_value(polymer, pairs):
    """Given the pairs and initial polymer calculate the score.

    Only counting left part of pair miss out on the last letter of the polymer.
    However, the last letter will always be the last letter of the initial
    polymer which we can add at the end!"""
    letter_count = defaultdict(int)
    for (a, b) in pairs:
        letter_count[a] += pairs[(a, b)]

    # Add last letter of the polymer to letter count
    letter_count[polymer[-1]] += 1

    values = list(letter_count.values())
    values.sort()
    return values[-1] - values[0]


pairs = defaultdict(int)

for i in range(1, len(polymer)):
    a, b = polymer[i - 1], polymer[i]
    pairs[(a, b)] += 1

for i in range(40):
    if i == 10:
        p1 = ans_value(polymer, pairs)

    NP = defaultdict(int)
    for (a, b) in pairs:
        m = R[(a, b)]
        count = pairs[(a, b)]
        NP[(a, m)] += count
        NP[(m, b)] += count

    pairs = NP


p2 = ans_value(polymer, pairs)

print(f"p1={p1}")
print(f"p2={p2}")
