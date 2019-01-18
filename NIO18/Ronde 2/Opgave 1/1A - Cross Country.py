class Player:
    def __init__(self, id, time):
        self.id = id
        self.time = time


players = {}
for i in range(1, int(input()) + 1):
    players[i] = Player(i, int(input()))

print(sorted(players.values(), key=lambda x: x.time)[0].id)
