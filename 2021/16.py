import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "16.in"

p1 = 0
p2 = 0

ptr = 0

xs = "".join([f"{int(ch, 16):04b}" for ch in open(filename).read().strip()])
# print(xs)
# print("VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB")

versions = []


def get_bits(program, ptr, count):
    n_ptr = ptr + count
    bits = program[ptr:n_ptr]
    return bits, n_ptr


def read_packet(program, ptr):
    global version

    version, ptr = get_bits(program, ptr, 3)
    version = int(version, base=2)
    versions.append(version)
    # print("version", version)

    # 4: literal value
    # other values are operators
    type_id, ptr = get_bits(program, ptr, 3)
    type_id = int(type_id, base=2)
    # print("type_id", type_id)

    # Parse literal value
    if type_id == 4:
        literal = ""
        while program[ptr] == "1":
            ptr += 1
            part, ptr = get_bits(program, ptr, 4)
            literal += part

        assert program[ptr] == "0"
        ptr += 1
        part, ptr = get_bits(program, ptr, 4)
        literal += part

        literal = int(literal, base=2)
        # print("literal", literal)
        return literal, ptr

    # Operator
    else:
        length_type, ptr = get_bits(program, ptr, 1)
        length_type = int(length_type)
        # print("length_type", length_type)

        vals = []
        if length_type == 0:
            # Total length in bits
            length, ptr = get_bits(program, ptr, 15)
            length = int(length, base=2)
            # print("length", length)

            start_ptr = ptr
            while ptr < start_ptr + length:
                res, ptr = read_packet(program, ptr)
                vals.append(res)
        else:
            assert length_type == 1
            # Number of sub-packets
            length, ptr = get_bits(program, ptr, 11)
            length = int(length, base=2)

            # print("num sub-packets", length)
            for _ in range(length):
                res, ptr = read_packet(program, ptr)
                vals.append(res)

        if type_id == 0:
            return sum(vals), ptr
        elif type_id == 1:
            res = 1
            for v in vals:
                res *= v
            return res, ptr
        elif type_id == 2:
            return min(vals), ptr
        elif type_id == 3:
            return max(vals), ptr
        elif type_id == 5:
            return 1 if vals[0] > vals[1] else 0, ptr
        elif type_id == 6:
            return 1 if vals[0] < vals[1] else 0, ptr
        elif type_id == 7:
            return 1 if vals[0] == vals[1] else 0, ptr
        assert False


p2, ptr = read_packet(xs, 0)  # Start reading the first packet
# print(ptr, len(xs))

# print(versions)
p1 = sum(versions)
print(f"p1={p1}")
print(f"p2={p2}")
