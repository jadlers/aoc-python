import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "1.in"
data = open(filename).read().strip()
X = [x.strip() for x in data.split("\n")]

mb = 14
mr = 12
mg = 13

p1 = 0
# p2 = 0


def possible_game(games, id):
    for game in games.split(";"):
        for color in [x.strip() for x in game.split(",")]:
            amnt, col = color.split(" ")
            amnt = int(amnt)
            if col == "red" and amnt > mr:
                print(id, amnt, col)
                return False
            elif col == "green" and amnt > mg:
                print(id, amnt, col)
                return False
            elif col == "blue" and amnt > mb:
                print(id, amnt, col)
                return False

    return True


for line in X:
    id, games = [x.strip() for x in line.split(":")]
    id = int(id.split(" ")[1])

    possible = possible_game(games, id)
    if possible:
        p1 += id


print(p1)
# print(p2)
