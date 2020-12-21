# MAXIMUM_POINTS_LENGTH = 10000
import time


def check_if_prime(n):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def check_if_gaussian_prime(x, y):
    gauss = False
    if x != 0 and y != 0:
        tmp = x ** 2 + y ** 2
        if check_if_prime(tmp):
            gauss = True

    if x == 0 and y != 0:
        tmp = abs(y)
        if check_if_prime(tmp) and tmp % 4 == 3:
            gauss = True

    if x != 0 and y == 0:
        tmp = abs(x)
        if check_if_prime(tmp) and tmp % 4 == 3:
            gauss = True

    return gauss


def get_points(m, min_x, min_y, max_x, max_y, x, y):
    global MAXIMUM_POINTS_LENGTH

    # M States:
    # 1: Right
    # 2: Up
    # 3: Left
    # 4: Down

    points = []

    start_x = x
    start_y = y

    if not check_if_gaussian_prime(start_x, start_y):
        return None

    valid = True

    x += 1

    while True:
        if not (min_x <= x <= max_x) or not (min_y <= y <= max_y):  # or len(points) >= MAXIMUM_POINTS_LENGTH:
            valid = False
            break

        if m == 1:
            if check_if_gaussian_prime(x, y):
                m += 1
                points.append([x, y])
                y += 1
            else:
                x += 1
        if m == 2:
            if check_if_gaussian_prime(x, y):
                m += 1
                points.append([x, y])
                x -= 1
            else:
                y += 1
        if m == 3:
            if check_if_gaussian_prime(x, y):
                m += 1
                points.append([x, y])
                y -= 1
            else:
                x -= 1
        if m == 4:
            if check_if_gaussian_prime(x, y):
                m = 1
                points.append([x, y])

                if x == start_x and y == start_y:
                    break

                x += 1
            else:
                y -= 1

    if valid:
        return points
    else:
        return None


def get_length(min_x, max_x, min_y, max_y, start_x, start_y):
    m = 1
    points = get_points(m, min_x, min_y, max_x, max_y, start_x, start_y)

    if not points:
        return 0

    x_len = 0
    y_len = 0

    for i in range(0, len(points) - 3, 4):
        x_len += abs(points[i][1] - points[i + 2][1])
        y_len += abs(points[i + 1][0] - points[i + 3][0])

    length = x_len + y_len
    return length * 2


min_x, max_x, min_y, max_y = [int(x) for x in input().split()]
start_x, start_y = [int(x) for x in input().split()]

start = time.time()
print(get_length(min_x, max_x, min_y, max_y, start_x, start_y))
print("This took: {0:.2f} ms".format((time.time() - start) * 1000))
