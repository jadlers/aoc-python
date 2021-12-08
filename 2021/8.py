import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

NUMS = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "acdfg": 3,
    "acdeg": 2,
    "abdfg": 5,
    "abdefg": 6,
    "abcefg": 0,
    "abcdfg": 9,
    "abcdefg": 8,
}


for line in open(filename):
    signal, output = line.strip().split("|")
    # print(signal)
    output_lengths = [len(s.strip()) for s in output.split()]
    simple_lengths = [x for x in output_lengths if x in [2, 3, 4, 7]]
    # print(pattern_lengths)
    # print(simple)
    p1 += len(simple_lengths)


print(f"p1={p1}")
print(f"p2={p2}")
