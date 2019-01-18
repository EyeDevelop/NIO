import itertools


def check(possibility, count):
    possibility = "".join(possibility)
    if "000" in possibility or "111" in possibility:
        return False

    if possibility.count("0") != count // 2:
        return False

    return True


count = int(input())
correct = []
for i in itertools.product("01", repeat=count):
    if check(i, count):
        correct.append("".join(i))


print(len(correct))
print("\n".join(correct))
