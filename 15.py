#!/usr/bin/env python3

import fileinput

for line in fileinput.input():
    print("NEW LINE", "=" * 30)
    xs = [int(x) for x in line.split(",")]

    last_spoken = {0: []}
    print(xs)

    turn = 0
    for (i, x) in enumerate(xs):
        last_spoken[x] = [i + 1]

    last = xs[-1]
    turn = len(xs) + 1  # NOTE: not sure
    print(turn)
    while turn <= 30000000:
        ls = last_spoken.get(last)
        if len(ls) >= 2:
            # Say last
            last = ls[-1] - ls[-2]
            if last in last_spoken:
                last_spoken[last].append(turn)
            else:
                last_spoken[last] = [turn]

        else:  # Say 0
            last_spoken[0].append(turn)
            last = 0

        if turn == 2020:
            # 249 correct for part 1
            print("2020 said:", last)
        elif turn == 30000000:  # Not pretty but it works. Took around 35s
            print("30000000 said:", last)

        # Inc turn
        turn += 1
