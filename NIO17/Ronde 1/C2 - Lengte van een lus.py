import math


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


x1, x2, y1, y2 = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
upward = False
pos = [a, b]
prev_pos = None
next_pos = None
method = 1
first = True
valid = False
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
            valid = True
            break

    if gauss:
        prev_pos = [pos[0], pos[1]]
        prev_length = length

if valid:
    print(str(lus_length))
else:
    print("0")
