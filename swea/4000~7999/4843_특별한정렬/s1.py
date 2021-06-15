import sys
sys.stdin = open('input.txt', 'r')



def bubble(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

T = int(input())

for tc in range(1, T+1):
    N = input()
    numbers = list(map(int, input().split()))

    numbers_up = bubble(numbers)                  # 오름차순 버블정렬
    numbers_down = sorted(numbers, reverse=True)  # 내림차순도 만들기엔 힘들어서.....

    result = []
    for i in range(10):
        # i가 홀수면 오름차순 정렬 => 내림차순에서 pop
        if i % 2:
            result.append(numbers_down.pop())
        # i가 짝수면 내림차순 정렬 => 오름차순에서 pop
        else:
            result.append(numbers_up.pop())
    print("#{}".format(tc), *result)

