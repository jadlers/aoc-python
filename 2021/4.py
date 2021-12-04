import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

# class Num:
#     def __init__(self, num)

class Board:
    def __init__(self, rows):
        self._rows = rows

    def __str__(self):
        s = ""
        for row in self._rows:
            s = s+str(row)+'\n'
            # print(s)
        return s
    
    def mark(self, num):
        for i, row in enumerate(self._rows):
            try:
                index = row.index((num, False))
                self._rows[i][index] = (num, True)
                return self.won()
            except ValueError:
                pass


    def won(self):
        for row in self._rows:
            # print('rrow', row)
            if all([x[1] for x in row]):
                return True
        cols = len(self._rows[0])
        for c in range(cols):
            vals = [x[c][1] for x in self._rows]
            if all(vals):
                return True

        return False

    def get_unchecked(self):
        res = []
        for row in self._rows:
            un = [x[0] for x in row if x[1] == False]
            # print(row, un)
            res.extend(un)

        return res



nums = []
boards = []
board = []
for i,line in enumerate(open(filename)):
    if i == 0:
        nums = [int(x) for x in line.strip().split(',')]
        continue
    elif i ==1:
        continue

    # Boards
    row = [(int(x), False) for x in line.strip().split()]
    # print(row)
    if len(row) > 0:
        board.append(row)
    else:
        boards.append(board)
        board = []
# Add last
boards.append(board)


for i,b in enumerate(boards):
    boards[i] = Board(b)
    # print(boards[i])


def part1(nums):
    for num in nums:
        # print(f'# {num}\n')
        for b in boards:
            won = b.mark(num)
            # print(b)
            if won:
                unchecked = b.get_unchecked()
                s = sum(unchecked)
                return s * num

def part2(nums):
    for num in nums:
        rem = []
        if len(boards) < 2:
            b = boards[0]
            won = b.mark(num)
            # print(b)
            if won:
                unchecked = b.get_unchecked()
                s = sum(unchecked)
                return s * num

        for b in boards:
            won = b.mark(num)
            # print(b)
            if won:
                rem.append(b)

        for r in rem:
            boards.remove(r)
            rem = []


p1 = part1(nums)
p2 = part2(nums)

print(f"p1={p1}")
print(f"p2={p2}")
