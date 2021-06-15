import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # # 버블 정렬
    # for i in range(len(numbers)-1, 0, -1):
    #     for j in range(0, i):
    #         if numbers[j] > numbers[j+1]:
    #             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    #
    # 선택 정렬
    for i in range(len(numbers)-1):
        min = i
        for j in range(i+1, len(numbers)):
            if numbers[min] > numbers[j]:
                min = j
        numbers[i], numbers[min] = numbers[min], numbers[i]

    print("#{}".format(tc), *numbers)