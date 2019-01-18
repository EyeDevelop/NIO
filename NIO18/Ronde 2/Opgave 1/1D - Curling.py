class Player:
    def __init__(self, id):
        self.id = id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_score(self):
        return sum(self.scores)


players = {}
times_to_run = int(input())
for i in range(times_to_run // 2):
    score_fplayer = int(input())
    score_splayer = int(input())

    if score_fplayer > score_splayer:
        player_id = 1
    else:
        player_id = 2

    points = (max(score_fplayer, score_splayer) - min(score_splayer, score_fplayer)) // 2000

    if player_id not in players.keys():
        players[player_id] = Player(player_id)
    players[player_id].add_score(points)

print(players[1].get_score())
print(players[2].get_score())
