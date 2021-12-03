import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

xs = [list(x.strip()) for x in open(filename)]

def create_columns(xs):
    cols = {}
    for x in xs:
        for (i, n) in enumerate(x):
            if i not in cols:
                cols[i] = {"list": []}
            cols[i]["list"].append(n)
    for col in cols.values():
        col['0'] = col['list'].count('0')
        col['1'] = col['list'].count('1')
    return cols

def oxy_rating(ys):
    idx = 0
    while len(ys) > 1:
        cols = create_columns(ys)
        common = '1' if cols[idx]['1'] >= cols[idx]['0'] else '0'
        # print(idx, common)
        ys = [y for y in ys if y[idx] == common]
        idx = (idx + 1) % len(ys[0])
        # print(ys)
    return int("".join(ys[0]), base=2)

def co2_rating(ys):
    idx = 0
    while len(ys) > 1:
        cols = create_columns(ys)
        common = '0' if cols[idx]['1'] >= cols[idx]['0'] else '1'
        ys = [y for y in ys if y[idx] == common]
        idx = (idx + 1) % len(ys[0])
    return int("".join(ys[0]), base=2)


p2 = (oxy_rating(xs)) * (co2_rating(xs))

print(f"p2={p2}")
