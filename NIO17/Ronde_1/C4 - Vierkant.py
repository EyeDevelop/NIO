import math


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


def check_square(max_x, max_y, x, y):
    start_x = x
    start_y = y

    x += 1

    if not check_if_gaussian_prime(start_x, start_y):
        return None

    while not check_if_gaussian_prime(x, y):
        x += 1

    length = abs(start_x - x)

    if length > 30:
        return None

    if start_x + length > max_x or start_y + length > max_y:
        return None

    if check_if_gaussian_prime(start_x + length, start_y)\
            and check_if_gaussian_prime(start_x, start_y + length)\
            and check_if_gaussian_prime(start_x + length, start_y + length):
        a = start_x
        b = start_y
    else:
        return None

    return [[a, b], length]

min_x, max_x, min_y, max_y = [int(x) for x in input().split()]

results = []
for i in range(min_y, max_y + 1):
    for j in range(min_x, max_x + 1):
        tmp = check_square(max_x, max_y, j, i)
        if tmp:
            results.append(tmp)

results = sorted(results, key=lambda x: x[1])
results = results[::-1]
results_fin = []
answer = 0
for i in range(len(results)):
    if results[i][0][1] == results[0][0][1]:
        results_fin.append(results[i])

if len(results_fin) > 1:
    distance = None
    for i in range(len(results_fin)):
        if not distance:
            distance = math.sqrt(results_fin[i][0][0] ** 2 + results_fin[i][0][1] ** 2)

        tmp = math.sqrt(results_fin[i][0][0] ** 2 + results_fin[i][0][1] ** 2)
        if tmp < distance:
            distance = tmp
            answer = results_fin[i][0][0] + results_fin[i][0][1]
else:
    answer = results_fin[0][0][0] + results_fin[0][0][1]

print(answer)
