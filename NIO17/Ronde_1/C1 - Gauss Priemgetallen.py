import math


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


for i in range(10):
    a, b = [int(x) for x in input().split()]

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

    if gauss:
        print("ja")
    else:
        print("nee")
