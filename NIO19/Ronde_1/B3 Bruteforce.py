import itertools
import threading
import time


def load_data():
    data = []
    with open("B3.csv", "rt") as fp:
        for line in fp:
            data.append(list(map(int, line.split(","))))

    return data


current_lowest = float('inf')
current_lowest_permutation = None
printing = True


def brute_force(data):
    global current_lowest, current_lowest_permutation

    for permutation in itertools.permutations(range(11), 9):
        c = 0
        for student in range(9):
            if len(data) - 1 >= student:
                c += data[student][permutation[student]]

        if c < current_lowest:
            current_lowest = c
            current_lowest_permutation = permutation


def print_current_highest():
    global current_lowest, current_lowest_permutation, printing

    while printing:
        print(f"\rCurrent lowest: {current_lowest} {current_lowest_permutation}", end="")
        time.sleep(.5)


threads = []


def main():
    global threads, printing

    data = load_data()

    t = threading.Thread(target=print_current_highest)
    t.start()
    threads.append(t)

    brute_force(data)

    printing = False
    t.join()

    print("\n\nDone!")
    print(current_lowest, current_lowest_permutation)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, Exception) as e:
        print(e)

        printing = False

        for thread in threads:
            thread.join()

        exit(0)
