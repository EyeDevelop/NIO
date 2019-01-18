class Player:
    def __init__(self, id):
        self.id = id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_highest_score(self):
        return max(self.scores)


players = {}
times_to_run = int(input())
for i in range(times_to_run // 2):
    players[i + 1] = Player(i + 1)
    players[i + 1].add_score(int(input()))

for i in range(times_to_run // 2):
    players[i + 1].add_score(int(input()))

print(sorted(players.values(), key=lambda x: x.get_highest_score(), reverse=True)[0].id)
