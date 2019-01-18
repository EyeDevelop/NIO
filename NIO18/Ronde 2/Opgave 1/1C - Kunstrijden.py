class Player:
    def __init__(self, id):
        self.id = id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_score(self):
        del self.scores[self.scores.index(max(self.scores))]
        del self.scores[self.scores.index(min(self.scores))]

        return sum(self.scores)


players = {}
times_to_run = int(input())

for i in range(times_to_run // 5):
    for j in range(5):
        if i + 1 not in players.keys():
            players[i + 1] = Player(i + 1)
        players[i + 1].add_score(int(input()))

sort = sorted(players.values(), key=lambda x: x.get_score(), reverse=True)
print(sort[0].id)
