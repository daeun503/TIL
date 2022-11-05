import sys
sys.stdin = open("input.txt", "r")

N = int(input())
IN = list(map(int, input().split()))

# 나, 상대 카드의 누적합 배열 구하기
my_acc, your_acc = [0], [0]
for i in range(N // 2):
    my_acc.append(my_acc[-1] + IN[2 * i])
    your_acc.append(your_acc[-1] + IN[2 * i + 1])

# 밑장빼기 => 밑장빼기하면 그 이후로 나와 상대의 카드가 바뀐다
# 특정 순간 이후로, 나와 상대의 값 차이가 가장 클 때 바꾼다
max_change_value = diff1 = diff2 = 0
for p in range(N // 2 + 1):
    # 밑장빼서 내 패와 바꾸기
    me_change_value = my_acc[-1] - my_acc[p]
    you_change_value = your_acc[-1] - your_acc[p]
    diff1 = you_change_value - me_change_value

    # 밑장빼서 상대 패와 바꾸기
    if p + 1 < N // 2:
        me_change_value = my_acc[-1] - my_acc[p + 1]
        you_change_value = your_acc[-2] - your_acc[p]
        diff2 = you_change_value - me_change_value

    # 나와 상대 값 차이가 가장 클 때 구하기
    max_change_value = max(max_change_value, diff1, diff2)


print(max(my_acc[-1], my_acc[-1] + max_change_value))
