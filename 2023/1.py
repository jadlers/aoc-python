import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "1.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

p1 = 0
for line in X:
    nums = [x for x in line if x.isnumeric()]
    l = int(nums[0] + nums[-1])
    p1 += l

print(p1)
