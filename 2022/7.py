import sys
from typing import Self, Any  # From python 3.11

# From Jonathan Paulson
filename = sys.argv[1] if len(sys.argv) > 1 else "7.in"
p1 = 0
p2 = 0


def cd(cwd: list[str], arg: str) -> list[str]:
    # note: Do not modify cwd
    if arg == "..":
        # print(cwd, "new path", cwd[:-1])
        return cwd[:-1]
    else:
        c = cwd.copy()
        c.append(arg)
        return c


def path(cwd: list[str]) -> str:
    return "/" + "/".join(cwd[1:])


X = [x.strip() for x in open(filename)]
S = {
    "/": {
        "size": 0,
        "parent": None,
        "files": {},  # {"name": "size"}
        "dirs": [],  # ["a", "e"]
    }
}

cur = []
for line in X:
    if line[0] == "$":
        parts = line.split()
        cmd = parts[1]
        arg = parts[2] if len(parts) > 2 else ""

        # print(cmd, arg)
        if cmd == "cd":
            cur = cd(cur, arg)
        elif cmd == "ls":
            # TODO Go through output
            pass
        continue

    # print(cur, "\tout:", line)
    # Only ls output here, know cwd
    parts = line.split()
    p = path(cur)
    if parts[0] == "dir":
        dir_name = parts[1]
        S[p]["dirs"].append(dir_name)
        S[f"{path(cd(cur, parts[1]))}"] = {
            "size": 0,
            "parent": p,
            "files": {},
            "dirs": [],
        }
    else:
        size, name = int(parts[0]), parts[1]
        S[p]["files"][name] = size

# for s in S:
#     print(s, S[s])
# print("parsing done")

# sort paths in depths
dirs = sorted([d for d in S], key=lambda p: p.count("/"), reverse=True)
# print(dirs)

dir_sizes = []

def dir_size(path):
    size = 0
    subdirs = [f"{path}/{d}" for d in S[path]["dirs"]]
    if path == "/":
        subdirs = [f"/{d}" for d in S[path]["dirs"]]
    size += sum([S[sub]["size"] for sub in subdirs])
    size += sum([S[path]["files"][name] for name in S[path]["files"]])
    dir_sizes.append(size)
    return size


for dir in dirs:
    if dir == "/":
        # Direct subdirs might not be calculated yet
        continue

    S[dir]["size"] = dir_size(dir)

S["/"]["size"] = dir_size("/")
for s in S:
    # print(s, S[s])
    cur = S[s]
    if cur["size"] > 100000:
        continue

    # print("adding total:", cur["size"])
    p1 += cur["size"]

needed = 30000000 - (70000000 - S["/"]["size"])
print(needed)
# print(sorted(dir_sizes))
for d in sorted(dir_sizes):
    if d >= needed:
        p2 = d
        break

print()
print(f"p1={p1}")
print(f"p2={p2}") # not: 37948890

# def traverse(path):
#     cur = S["/"]
#     for dir in path[1:].split("/")[1:]:
#         print(f"traversing '{dir}'")
#         if dir in cur:
#             cur = dir
#         else:
#             cur[dir] = {}

#     print(S, cur)


# class FileTree:
#     parent: Self = None
#     name = ""
#     size = 0
#     # Shouldn't differ I know
#     dirs = {}  # {"a": FileTree}
#     files = {}

#     def __init__(self, parent, name, size=0):
#         self.parent: Self @ FileTree = parent
#         self.name = name
#         self.size = size

#     def __str__(self):
#         dir_names = [k for k in self.dirs]
#         return f"{self.parent} | {self.size} | dirs={dir_names}"

#     def path(self):
#         t = self
#         p = []
#         while t.parent != None:
#             break

#     def cd(self, arg):
#         if arg == "/":
#             return self  # Only first line

#         if arg == "..":
#             return self.parent
#         elif arg in self.dirs:
#             new = self.dirs[arg]
#             print("new", new, new.parent)
#             return new

#         assert False

#     def mkdir(self, name):
#         new_dir = FileTree(parent=self, name=name)
#         print(f"created dir ({new_dir})")
#         self.dirs[name] = new_dir

#     def touch(self, name, size):
#         self.files[name] = FileTree(name, self, size)


# root = FileTree(None, "/")
# C = root
