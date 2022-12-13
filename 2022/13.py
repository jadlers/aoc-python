import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "13.in"
p1 = 0
p2 = 0


data = open(filename).read().strip()
X = [x.strip() for x in open(filename)]


def conv(a, b):
    if type(a) == list:
        return a, [b]
    return [a], b


def comp(a, b):
    # print("comp", a, b)
    ret = None
    for e1, e2 in zip(a, b):
        # print(e1,e2)
        if type(e1) != type(e2):
            # print("mixed type convert", e1, e2)
            e1, e2 = conv(e1, e2)
            ret = comp(e1, e2)
        elif type(e1) == list:  # Both lists
            ret = comp(e1, e2)
        elif e1 < e2:
            print("correect - left smaller!")
            return True  # Found it
        elif e2 < e1:
            print("NOPE - right smaller!")
            return False

        if ret != None:
            return ret

    la = len(a)
    lb = len(b)
    if la < lb:
        print("correect - left smaller")
        return True
    elif la > lb:
        print("NOPE - right side is smaller")
        return False

    return ret


for i, packet in enumerate(data.split("\n\n")):
    i += 1
    a, b = [eval(p.strip()) for p in packet.split("\n")]
    print(a, b)
    ret = comp(a, b)
    if ret:
        p1 += i
    assert ret != None
    print(ret)

print(f"p1={p1}")  # Not: 5930
print(f"p2={p2}")
