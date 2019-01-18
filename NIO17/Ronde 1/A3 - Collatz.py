n = int(input())

ar = []
if n <= 1:
    print(n)
else:
    while n > 1:
        ar.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (n*3)+1

    print(max(ar))
