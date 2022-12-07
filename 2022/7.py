import sys

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "7.in"
p1 = 0
p2 = 0


def cd(dirs: list[str], arg: str) -> list[str]:
    # note: Do not modify cwd
    if arg == "..":
        return dirs[:-1]
    else:
        # Would change list passed otherwise, no longer a problem
        c = dirs.copy()
        c.append(arg)
        return c


def path(dirs: list[str]) -> str:
    """`path` take a list of directories from the root, which is `/`, and
    return the string representation of the path. The `path` will **always**
    start with `/`.

    Examples:
    - [] -> "/"
    - ["a", "b", "c"] -> "/a/b/c"
    """
    return "/" + "/".join(dirs[1:])


def dir_size(path: str) -> int:
    """`dir_size` calculates the size of the directory in the path.

    The size of subdirectories is calculated recursively if the size is not
    already known.
    """
    if S[path]["size"]:
        return S[path]["size"]

    size = 0
    size += sum([S[path]["files"][name] for name in S[path]["files"]])

    # Calculate size for subdirectories recursively
    size += sum([dir_size(sub) for sub in S[path]["dirs"]])
    dir_sizes.append(size)  # For p2, add to list of dir sizes

    S[path]["size"] = size  # Store the size of the path for later calculations
    return size


S = {
    "/": {
        "size": None,
        "files": {},  # {"name": "size"}
        "dirs": [],  # ["/a", "/a/e/longer"]
    }
}

cwd = []
for line in [x.strip() for x in open(filename)]:
    if line[0] == "$":
        parts = line.split()
        cmd = parts[1]
        if cmd == "cd":
            arg = parts[2]
            cwd = cd(cwd, arg)

        # We only care about the output from ls which is the only other command
        continue

    # Only ls output here, know cwd
    parts = line.split()
    p = path(cwd)
    if parts[0] == "dir":
        dir_path = f"{p}/{parts[1]}" if p != "/" else f"/{parts[1]}"
        S[p]["dirs"].append(dir_path)
        S[dir_path] = {
            "size": None,
            "files": {},
            "dirs": [],
        }
    else:  # It's a file
        size, name = int(parts[0]), parts[1]
        S[p]["files"][name] = size

# sort paths on depth in descending order to make sure the correct total size
# will be calculated. Read documentation for `dir_size` for more information.
# We always want to calculate for the root last.
dirs = sorted([d for d in S], key=lambda p: p.count("/"), reverse=True)
dir_sizes = []


# Calculating the root will recursively calculate all subdirectories
dir_size("/")
for s in S:
    cur = S[s]
    if cur["size"] > 100000:
        continue

    p1 += cur["size"]

# P2
REQUIRED = 30000000
ENTIRE_DISK = 70000000
current_usage = S["/"]["size"]
needed = REQUIRED - (ENTIRE_DISK - current_usage)

# Kind of like find in js
# See: https://stackoverflow.com/a/10302859
p2 = next((x for x in sorted(dir_sizes) if x >= needed), None)


print()
print(f"p1={p1}")
print(f"p2={p2}")  # not: 37948890
