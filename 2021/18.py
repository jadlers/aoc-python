import sys
import os


def DEB(*args):
    """Print if environment environment `DEBUG` is set"""
    if os.getenv("DEBUG"):
        print(*args)


# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "18.in"

p1 = 0
p2 = 0

def closing_bracket(xs):
    open = 1
    for i, x in enumerate(xs):
        if i == 0:
            continue
        if x == "[":
            open += 1
        elif x == "]":
            open -= 1

        if open == 0:
            return i

    return -1


def parse_num(input: str):
    DEB(f"parse_num({input})")
    if input[0] == "[":
        comma = 2  # 1 = digit, 2 = ','
        if len(input) > 1 and input[1] == "[":
            cl = closing_bracket(input[1:])
            comma = cl + 2  # The comma separating fst & snd
            assert input[comma] == ",", f"was {input[comma]}"

        DEB(f"input={input} comma={comma} ({input[comma]})")
        assert input[comma] == ","

        fst_inp = input[1:comma]
        snd_inp = input[comma + 1 :]
        # DEB("Parsing split into:", fst_inp, "|", snd_inp)
        fst = parse_num(fst_inp)
        snd = parse_num(snd_inp)
        return [fst, snd]
    else:
        return int(input[0])


def literals(num):
    xs = []
    for el in num:
        if isinstance(el, list):
            xs.extend(literals(el))
        else:
            xs.append(el)
    return xs


def reduce(num):
    # 1. If any pair is nested inside four pairs, the leftmost such pair explodes.
    fst, snd = num
    Q = []
    max_depth = 1
    if isinstance(fst, list):
        Q.append((fst, max_depth))
    if isinstance(snd, list):
        Q.append((snd, max_depth))

    while Q:
        element, depth = Q.pop(0)
        DEB("Now at", element, Q)
        for el in element:
            if isinstance(el, list):
                Q.append((el, depth + 1))
                max_depth = max(max_depth, depth + 1)
                if depth + 1 >= 4:
                    DEB("explode", el, num, literals(num))
    DEB(max_depth)

    # If any regular number is 10 or greater, the leftmost such regular number splits.

    # Not reduced
    return num, False


def addition(n1, n2):
    new_num = [n1, n2]

    new_num, reduced = reduce(new_num)
    while reduced:
        new_num, reduced = reduce(new_num)

    return [n1, n2]


numbers = []
for line in open(filename):
    numbers.append(parse_num(line.strip()))

# DEB(addition(numbers[0], numbers[1]))
DEB("reduce: '[[[[[9,8],1],2],3],4]'", reduce([[[[[9, 8], 1], 2], 3], 4]))


print(f"p1={p1}")
print(f"p2={p2}")
