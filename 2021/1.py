import fileinput

xs = [int(x.strip()) for x in fileinput.input()]

inc = 0

last = xs[0]
for x in xs[1:]:
    if x > last:
        inc += 1
    last = x

print(f"p1: {inc}")

inc2 = 0
for i in range(len(xs) - 3):
    # if xs[i] + xs[i+1] + xs[i+2] < xs[i+1] + xs[i+2] + xs[i+3]:
    if xs[i] < xs[i + 3]:
        inc2 += 1

print(f"p2: {inc2}")
