class Player:
    def __init__(self, id, distances):
        self.id = id
        self.speeds = {}

        if not distances or len(distances) == 0:
            distances = [1000, 1000, 1000, 1000, 1000]

        distance_names = [500, 1000, 1500, 5000, 10000]
        for distance_index in range(len(distances)):
            self.speeds[distance_names[distance_index]] = distances[distance_index]

    def get_speed(self, distance):
        return self.speeds[distance]


players = {}
for i in range(1, int(input()) + 1):
    players[i] = Player(i, [float(x) for x in input().split()])

lowest = {}
times_to_run = {
    500: 4,
    1000: 4,
    1500: 4,
    5000: 3,
    10000: 3
}
for i in [500, 1000, 1500, 5000, 10000]:
    sort = sorted(players.values(), key=lambda x: x.get_speed(i))
    lowest[i] = sort[:times_to_run[i]]

for distance in [500, 1000, 1500, 5000, 10000]:
    for player in lowest[distance]:
        print(player.id)
