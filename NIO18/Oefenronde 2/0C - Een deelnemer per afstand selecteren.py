import sys, time

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
for i in [500, 1000, 1500, 5000, 10000]:
    sort = sorted(players.values(), key=lambda x: x.get_speed(i))
    lowest[i] = sort[0]

    del players[sort[0].id]

for i in [500, 1000, 1500, 5000, 10000]:
    print(lowest[i].id)
