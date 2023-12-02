import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "1.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

# Max number of each cube in P1
mb = 14
mr = 12
mg = 13


def possible_game(games):
    for game in games.split(";"):
        for color in [x.strip() for x in game.split(",")]:
            amnt, col = color.split(" ")
            amnt = int(amnt)
            if col == "red" and amnt > mr:
                return False
            elif col == "green" and amnt > mg:
                return False
            elif col == "blue" and amnt > mb:
                return False

    return True


def min_cubes(games):
    max_r, max_g, max_b = 0, 0, 0
    for game in games.split(";"):
        for color in [x.strip() for x in game.split(",")]:
            amnt, col = color.split(" ")
            amnt = int(amnt)
            if col == "red" and amnt > max_r:
                max_r = amnt
            elif col == "green" and amnt > max_g:
                max_g = amnt
            elif col == "blue" and amnt > max_b:
                max_b = amnt
    return max_r * max_g * max_b


p1 = 0
for line in X:
    id, games = [x.strip() for x in line.split(":")]
    id = int(id.split(" ")[1])

    possible = possible_game(games)
    if possible:
        p1 += id


p2 = 0
for line in X:
    id, games = [x.strip() for x in line.split(":")]
    id = int(id.split(" ")[1])
    p2 += min_cubes(games)


print(p1)
print(p2)
