import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "2.in"
p1 = 0
p2 = 0

hi = None
lo = None

class Node:
    def __init__(self, data, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

    def __str__(self):
        p = self._prev.data() if self._prev is not None else "_"
        n = self._next.data() if self._next is not None else "_"
        return f"{p} <- ({self._data}) -> {n}"

    def data(self):
        return self._data

    def next(self):
        return self._next

    def set_next(self, node):
        self._next = node

    def prev(self):
        return self._prev

    def set_prev(self, node):
        self._prev = node

def print_ring(start, start3=True):
    if start3:
        start = find_node(start, 3)
    start_d = start.data()

    print(f'{start_d} - ', end='')
    c = start.next()
    while c.data() != start_d:
        print(f'{c.data()} - ', end='')
        c = c.next()

    print(start_d)

def find_node(start, target: int):
    """Find the node with target data given a node as a starting point.

    Note that it will loop forever if the target doesn't exist."""
    while start.data() != target:
        start = start.next()
        if start is None:
            sys.exit(1)
    return start

def pickup3(start):
    """Remove and return the 3 nodes directly clockwise from `start`.

    The ring is closed together and the first node of the three removed ones is
    returned. The fist and last removed nodes has their prev/next removed"""
    fst = start.next()
    fst.set_prev(None) #Remove reference to original ring

    after = fst
    # Jump 3 nodes ahead to the Node **after** the deleted ones
    last = None
    for i in range(3):
        if i == 2:
            last = after
        after = after.next()
    last.set_next(None) # Remove the reference to the original ring

    # Close the ring again
    start.set_next(after)
    after.set_prev(start)

    # NOTE: The first/last of the deleted Nodes have incorrect prev/next Node
    return fst

def place(split_left, cups):
    """Inserts the `cups` right next to the `split_left`.

    Before: split_left - split_right - ... - split_left
    After:  split_left - cups - split_right - ... split_left
    """
    split_right = split_left.next()
    # print(f'sl={split_left}\nsr={split_right}')

    split_left.set_next(cups)
    end_cups = ll_end(cups)
    end_cups.set_next(split_right)

    return split_left

    
def ll_end(start):
    while start.next() is not None:
        start = start.next()
    return start

def ll_includes(start, target):
    while start is not None:
        if start.data() == target:
            return True
        start = start.next()

    return False

def ll_print(start):
    while start.next() is not None:
        print(f'{start.data()} - ', end='')
        start = start.next()
    print(start.data())


def select_destination(curr, removed) -> int:
    num = curr.data() - 1
    if num < lo:
        num = hi
    print(f'potential target={num}')
    while ll_includes(removed, num):
        num -= 1
        
        print(f'potential target={num}')
        # If the num 
        if num < lo:
            num = hi

    if num < lo:
        num = hi
    return num

def move(curr):
    removed = pickup3(curr)
    print('pick up=', end='')
    ll_print(removed)
    dest = select_destination(curr, removed)
    print(f'dest={dest}')
    place_target = find_node(curr, dest)
    # print(curr)
    place(place_target, removed)
    # print_ring(curr)
    return curr.next() # Advance the current cup by one


def answer(curr):
    nums = []
    curr = find_node(curr, 1).next()

    while curr.data() != 1:
        nums.append(curr.data())
        curr = curr.next()

    print(nums)
    return ''.join([str(s) for s in nums])

xs = [int(x) for x in list(open(filename).readline().strip())]
last = None
for num in xs:
    num = int(num)
    n = Node(num)
    if last is not None:
        n.set_prev(last)
        last.set_next(n)

    if hi is None or num > hi:
        hi = num
    if lo is None or num < lo:
        lo = num

    last = n
# print(f'lo={lo} hi={hi}')

# Find first and close the ring by attaching last and first
first = last
while first.prev() is not None:
    first = first.prev()

first.set_prev(last)
last.set_next(first)


# START OF GAME
curr = first
print(f' is {curr}')
for i in range(100):
    print(f'-- move {i+1} curr={curr.data()} --')
    print_ring(curr)
    curr = move(curr)

begin = find_node(curr, 1)
print_ring(begin, start3=False)

p1 = answer(curr)


print(f"p1={p1}")
# NOTE: Not 97865432
# print(f"p2={p2}")
