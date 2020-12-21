import math, sys, threading


def check_if_prime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    _i = 5
    while _i ** 2 <= n:
        if n % _i == 0 or n % (_i + 2) == 0:
            return False
        _i += 6
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
    pos_x, pos_y = (a + 1, b)
    points = [[a, b]]
    method = 1
    up = False
    valid = False
    while x1 <= pos_x <= x2 and y1 <= pos_y <= y2:
        if not up:
            if check_if_gaussian_prime(pos_x, pos_y):
                points.append([pos_x, pos_y])

                up = True
                pos_y += method
                continue
            pos_x += 1 * method

        else:
            if check_if_gaussian_prime(pos_x, pos_y):
                points.append([pos_x, pos_y])

                up = False
                method *= -1
                pos_x += method
                continue
            pos_y += method

        if len(points) >= 4:
            if points[len(points) - 2] == points[0] and points[len(points) - 1] == points[1]:
                valid = True
                break

    del points[len(points) - 2]
    del points[len(points) - 1]

    length = 0
    if valid:
        i = 0
        while i < len(points) - 1:
            dif_x = abs(abs(points[i][0]) - abs(points[i+1][0]))
            dif_y = abs(abs(points[i][1]) - abs(points[i+1][1]))

            length += dif_x + dif_y
            i += 1
        length += abs(abs(points[len(points) - 1][0]) - abs(points[0][0])) + abs(abs(points[len(points) - 1][1]) - abs(points[0][1]))
    return length

biggest = 0
current = 0
def run():
    global biggest
    global current
    for i in range(0, 6001):
        for j in range(0, 6001):
            length = get_length(j - 1000, j + 1000, i - 1000, i + 1000, j, i)
            if length > biggest:
                biggest = length

            current += (i + j)

geheel = (6001 - 1)**2 * (6001 - 1 + 0)
while current < geheel:
    sys.stdout.write("\r{:.2f}%, Current largest: {}".format(current / geheel * 100, biggest))
    sys.stdout.flush()
