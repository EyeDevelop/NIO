class Player:
    def __init__(self, id):
        self.id = id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_score(self):
        return sum(self.scores)


players = {}

# Input
times_to_run = int(input())
player_order = list(range(1, (times_to_run // 4) + 1))

for i in range(4):
    for j in player_order:
        if j not in players.keys():
            players[j] = Player(j)

        players[j].add_score(int(input()))

    player_order = sorted(players.keys(), key=lambda x: players[x].get_score(), reverse=True)
    pass

# Scoring
sort = sorted(players.values(), key=lambda x: x.get_score())
print(sort[0].id)
