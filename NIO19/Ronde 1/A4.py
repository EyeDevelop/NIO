n = int(input())

if n in [1, 3, 9]:
    print(n)
    exit()

TIMES_TO_RUN = 10**6

main_rivers = {
    1: [1],
    3: [3],
    9: [9]
}

river_of_n = [n]

while True:
    n1 = main_rivers[1][-1] + sum(map(int, list(str(main_rivers[1][-1]))))
    main_rivers[1].append(n1)

    n2 = main_rivers[3][-1] + sum(map(int, list(str(main_rivers[3][-1]))))
    main_rivers[3].append(n2)

    n3 = main_rivers[9][-1] + sum(map(int, list(str(main_rivers[9][-1]))))
    main_rivers[9].append(n3)

    if min(n1, n2, n3) >= 5 * n:
        break

for i in range(TIMES_TO_RUN):
    n1 = main_rivers[1][-1] + sum(map(int, list(str(main_rivers[1][-1]))))
    main_rivers[1].append(n1)

    n2 = main_rivers[3][-1] + sum(map(int, list(str(main_rivers[3][-1]))))
    main_rivers[3].append(n2)

    n3 = main_rivers[9][-1] + sum(map(int, list(str(main_rivers[9][-1]))))
    main_rivers[9].append(n3)

    nn = river_of_n[-1] + sum(map(int, list(str(river_of_n[-1]))))
    river_of_n.append(nn)

    if nn in main_rivers[1]:
        print(1)
        print(nn)
        break
    elif nn in main_rivers[3]:
        print(3)
        print(nn)
        break
    elif nn in main_rivers[9]:
        print(9)
        print(nn)
        break
