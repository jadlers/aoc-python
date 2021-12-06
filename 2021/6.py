import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0
M = [0 for _ in range(9)]


def step(A):
    B = [0 for _ in range(9)]
    for i in range(9):  # 8 largest num
        if i == 0:
            B[6] += A[0]
            B[8] += A[0]
        else:
            B[i - 1] += A[i]

    return B


xs = [int(x) for x in open(filename).readline().strip().split(",")]
for x in xs:
    M[x] += 1


# Part1
for i in range(80):
    M = step(M)
p1 = sum(M)

# Part 2
for i in range(256 - 80):
    M = step(M)
p2 = sum(M)


print(f"p1={p1}")
print(f"p2={p2}")
