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
for i in range(times_to_run // 5):
    time = int(input())
    shots_missed = []

    for j in range(4):
        shot_res = int(input())
        if 5000 <= shot_res <= 9999:
            shots_missed.append(0)
        elif 2000 <= shot_res <= 4999:
            shots_missed.append(1)
        elif 500 <= shot_res <= 1999:
            shots_missed.append(2)
        elif 0 <= shot_res <= 499:
            shots_missed.append(3)

    if i + 1 not in players.keys():
        players[i + 1] = Player(i + 1)

    players[i + 1].add_score(time + sum(shots_missed) * 1000)

# Scoring
sort = sorted(players.values(), key=lambda x: x.get_score())
print(sort[0].id)
