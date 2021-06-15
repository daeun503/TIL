import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    money = int(input())
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * 8

    # result[idx]: 해당 화폐 몇 장 들어가는지. money: 해당 화폐 빼고 잔돈
    for idx, unit in enumerate(units):
        result[idx] = money // unit
        money = money % unit

    print('#{}'.format(tc))
    print(*result)