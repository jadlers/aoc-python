import fileinput

ops = [x.strip().split(" ") for x in fileinput.input()]


def run(ops):
    fp = 0
    acc = 0
    visited = [False] * len(ops)

    for _ in range(len(ops)):

        if fp == len(ops) or visited[fp]:
            break
        else:
            visited[fp] = True

        op = ops[fp]
        # print(op)

        if op[0] == "nop":
            fp += 1
        elif op[0] == "acc":
            acc += int(op[1])
            fp += 1
        elif op[0] == "jmp":
            fp += int(op[1])

    return acc, fp


(p1, _) = run(ops)
print(p1)

p2 = None

for i in range(len(ops)):

    op = ops[i]
    if op[0] not in ["jmp", "nop"]:
        # print(f"skipping {op}")
        continue

    prev = op[0]
    if op[0] == "nop":
        op[0] = "jmp"
    elif op[0] == "jmp":
        op[0] = "nop"

    res, fp = run(ops)

    # print(fp, res)
    if fp == len(ops):
        p2 = res
        break

    op[0] = prev

print(p2)
