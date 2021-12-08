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


signals = []  # 2D: Each number appears once in every list
outputs = []
for line in open(filename):
    signal, output = line.strip().split("|")
    signals.append([s.strip() for s in signal.strip().split()])
    outputs.append([s.strip() for s in output.strip().split()])

    # P1
    output_lengths = [
        len(s.strip()) for s in output.split() if len(s.strip()) in [2, 3, 4, 7]
    ]
    p1 += len(output_lengths)

# The following line should map to
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
#  dddd    aaaa
# e    a  b    c
# e    a  b    c
#  ffff    dddd
# g    b  e    f
# g    b  e    f
#  cccc    gggg

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

#   1:       4:      7:      8:
#  ....     ....    aaaa    aaaa
# .    c   b    c  .    c  b    c
# .    c   b    c  .    c  b    c
#  ....     dddd    ....    dddd
# .    f   .    f  .    f  e    f
# .    f   .    f  .    f  e    f
#  ....     ....    ....    gggg


# a: 7 - 1 Difference between 1 and 7
# b: 0 - 2 - 1
# c: 4 - 5


def intersection(a, b):
    return [ch for ch in a if ch in b]


segments = "abcdefg"


def decode(signals, outputs):
    M: dict[int, str] = {}  # Map from [number] -> [input signal]
    for signal in signals:
        sl = len(signal)
        if sl == 2:
            M[1] = signal
        elif sl == 3:
            M[7] = signal
        elif sl == 4:
            M[4] = signal
        elif sl == 7:
            M[8] = signal

    # The one with five segments including both used for 1 is 3
    for signal in [s for s in signals if len(s) == 5]:
        if len(intersection(signal, M[1])) == 2:
            M[3] = signal
            break

    # The one with six segments including union of 4 and 7 must be 9
    union47 = list(set.union(set(M[4]), set(M[7])))
    for signal in [s for s in signals if len(s) == 6]:
        missing = 0
        for ch in signal:
            if ch not in union47:
                missing += 1
        if missing == 1:
            M[9] = signal

    # remaining: 0, 6 (len 6)
    for signal in [s for s in signals if len(s) == 6 and s not in M.values()]:
        # 0 only intersects with one segment of 1
        if len(intersection([ch for ch in signal], M[1])) == 1:
            M[6] = signal
        else:
            M[0] = signal

    # remaining: 2, 5 (len 5)
    for signal in [s for s in signals if len(s) == 5 and s not in M.values()]:
        if len(intersection([ch for ch in signal], M[4])) == 3:
            M[5] = signal
        else:
            M[2] = signal

    N = {}
    for m in M:
        N["".join(sorted(M[m]))] = m

    res = []
    for output in outputs:
        res.append(str(N["".join(sorted(output))]))

    val = int("".join(res))
    # print(val, outputs)
    return val


for i in range(len(outputs)):
    p2 += decode(signals[i], outputs[i])

print(f"p1={p1}")
print(f"p2={p2}")
