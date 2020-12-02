#!/usr/bin/env python3

import fileinput
from math import floor

# 25x6 for real input
w = 25
h = 6

# p1
# w = 3
# h = 2

# p2
# w = 2
# h = 2

data = fileinput.input().__next__().strip()
layer_size = w * h
num_layers = int(len(data) / layer_size)
# print(num_layers)

layers = [
    [data[j : j + w] for j in range(i, i + layer_size, w)]
    for i in range(0, len(data), layer_size)
]


def count_char(l, ch):
    return sum(1 for i in l if i == ch)


least_zeroes_num = layer_size
least_zeroes_layer = 0
for l_idx in range(len(layers)):
    layer = layers[l_idx]
    zeroes = sum([count_char(row, "0") for row in layer])
    # print("layer:", layer)
    # print("zeroes:", zeroes)
    if zeroes < least_zeroes_num:
        # print("Setting new zeroes leader", l_idx)
        least_zeroes_layer = l_idx
        least_zeroes_num = zeroes

ones = 0
twos = 0
for row in layers[least_zeroes_layer]:
    ones += count_char(row, "1")
    twos += count_char(row, "2")


# print(layers[least_zeroes_layer])
p1 = ones * twos
print("p1:", p1)  # 1656 too high, 1330 correct

# Prepare the image array
image = [0] * h
for row in range(h):
    image[row] = [0] * w


def determine_pixel(lay_pxs):
    idx = 0
    while lay_pxs[idx] == "2":
        idx += 1
    return lay_pxs[idx]


for row in range(h):
    # print("row:", row)
    for col in range(w):
        # print("col:", col)
        pixels = [layers[layer_idx][row][col] for layer_idx in range(0, len(layers))]
        # print(pixels)
        # print("pix:", determine_pixel(pixels))
        image[row][col] = determine_pixel(pixels)

print("p2:")
for row in image:
    # print(row, sep="")
    for col in row:
        if col == "1":
            print("X", end="")
        else:
            print(" ", end="")
    print()
