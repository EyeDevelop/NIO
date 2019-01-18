import math
import sys
import threading


def check_if_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def check_if_gaussian_prime(a, b):
    gauss = False
    if a != 0 and b != 0:
        tmp = a ** 2 + b ** 2
        if check_if_prime(tmp):
            gauss = True

    if a == 0 and b != 0:
        tmp = math.fabs(b)
        if check_if_prime(tmp) and tmp % 4 == 3:
            gauss = True

    if a != 0 and b == 0:
        tmp = math.fabs(a)
        if check_if_prime(tmp) and tmp % 4 == 3:
            gauss = True

    return gauss


def get_length(x1, x2, y1, y2, a, b):
    upward = False
    pos = [a, b]
    prev_pos = None
    next_pos = None
    method = 1
    first = True
    lus_length = 0
    length = 0
    prev_length = 0
    while x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
        gauss = False

        if first and next_pos is not None:
            first = False
        if not upward:
            pos[0] += 1 * method
            if check_if_gaussian_prime(pos[0], pos[1]):
                lus_length += length
                prev_length = length
                length = 1
                upward = True
                if first:
                    next_pos = [pos[0], pos[1]]
                gauss = True
            else:
                length += 1
        else:
            pos[1] += 1 * method
            if check_if_gaussian_prime(pos[0], pos[1]):
                lus_length += length
                prev_length = length
                length = 1
                upward = False
                if method == -1:
                    method = 1
                elif method == 1:
                    method = -1
                gauss = True
            else:
                length += 1

        if not first:
            if pos[0] == next_pos[0] and pos[1] == next_pos[1] and prev_pos[0] == a and prev_pos[1] == b:
                lus_length -= (prev_length - length)
                return lus_length

        if gauss:
            prev_pos = [pos[0], pos[1]]
    return 0


def get_lengths_in_area(startx, starty, area):
    global glob_x, glob_y
    for i in range(starty, area + 1):
        for j in range(startx, area + 1):
            if check_if_gaussian_prime(i, j):
                tmp = threading.Thread(target=run_threaded, args=(i, j,))
                tmp.start()
            glob_y = i
            glob_x = j


def run_threaded(i, j):
    global lussen
    tmp = get_length(0, 6000, 0, 6000, i, j)
    if tmp != 0 and tmp not in lussen:
        lussen.append(tmp)

lussen = []

glob_x, glob_y = 0, 0

x, y = [int(i) for i in input().split()]

t1 = threading.Thread(target=get_lengths_in_area, args=(x, x, y,))
t1.start()

while threading.active_count() > 1:
    if len(lussen) >= 1:
        themax = max(lussen)
    else:
        themax = 0
    sys.stdout.write("\rCurrent active threads: {}; Current longest: {}; Current maximum coords: ({}, {})".format(threading.active_count(), themax, glob_x, glob_y))
    sys.stdout.flush()

print()
print("Result: {}".format(max(lussen)))
