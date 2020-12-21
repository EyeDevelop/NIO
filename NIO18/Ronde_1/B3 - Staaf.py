import threading
import time
import random

length = 25
val = 350

profit = [
    20,
    37,
    42,
    67,
    72,
    98,
    116,
    122,
    142,
    152,
    153,
    175,
    182,
    214,
    215,
    240,
    245,
    267,
    275,
    286,
    293,
    311,
    331,
    340,
    350
]
for i in range(len(profit)):
    print("%d: %s" % (i + 1, round(profit[i] / (i + 1), 2)))


highest = (0, {})
threads = []


def interrupt(threads_to_stop):
    Controller.can_work = False
    Controller.can_print = False

    for t in threads_to_stop:
        t.join()

    with open("B3 - Result.txt", 'w') as fp:
        print("Highest: %d\nCombination: %s" % (highest[0], highest[1]), file=fp)

    print("Highest written to file.")


class Controller:
    print_con = threading.Condition()
    can_print = True

    work_con = threading.Condition()
    can_work = True


class Printer(threading.Thread):
    def run(self):
        while True:
            with Controller.print_con:
                if not Controller.can_print:
                    Controller.print_con.wait()

                self.do_print()

    def do_print(self):
        global highest
        global threads

        coll = {}

        for i in highest[1].keys():
            if highest[1][i]:
                coll[i] = highest[1][i]

        thread_work = [t.last_attempt for t in threads][:20]

        print("\rHighest: %d; Coll: %s; Threads: %s" % (highest[0], coll, thread_work), end="")
        time.sleep(.2)


class Worker(threading.Thread):
    def __init__(self):
        super().__init__()
        self.coll = {}
        self.reset_coll()

        self.last_attempt = 0

    def run(self):
        while True:
            with Controller.work_con:
                if not Controller.can_work:
                    Controller.work_con.wait()

                self.do_calculate()

    def reset_coll(self):
        self.coll = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 0,
            15: 0,
            16: 0,
            17: 0,
            18: 0,
            19: 0,
            20: 0,
            21: 0,
            22: 0,
            23: 0,
            24: 0
        }

    def do_calculate(self):
        global highest
        global profit

        self.reset_coll()

        c = 25
        while c > 0:
            ind = random.randint(1, c if c < 25 else 24)

            if ind > c:
                continue

            self.coll[ind] += 1
            c -= ind

        s = 0
        cost = (sum(self.coll.values()) - 1) * 5
        for i in self.coll.keys():
            s += profit[i - 1] * self.coll[i]

        t = s - cost
        if t > highest[0]:
            highest = (t, self.coll)

        self.last_attempt = t


if __name__ == "__main__":
    for _ in range(int(input("Amount of threads: "))):
        threads.append(Worker())

    p = Printer()
    p.start()

    for t in threads:
        t.start()
