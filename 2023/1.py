import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "1.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

p1 = 0
p2 = 0
for line in X:
    nums = [x for x in line if x.isnumeric()]

    # Required for part 2 sample input
    if len(nums) == 0:
        continue
    l = int(nums[0] + nums[-1])
    p1 += l

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in X:
    nums = []
    i = 0
    while i < len(line):
        if line[i].isnumeric():
            nums.append(int(line[i]))
            i += 1
            continue

        # Check if letter is beginning of word representation
        for v, w in enumerate(words):
            if line[i:].startswith(w):
                nums.append(v + 1)
                i += 1
                break
        i += 1

    p2 += int(f"{nums[0]}{nums[-1]}")


print(p1)
print(p2)
