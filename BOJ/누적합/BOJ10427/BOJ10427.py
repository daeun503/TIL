import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    money = list(map(int, input().split()))
    N = money.pop(0)
    money.sort()

    # money의 누적합 acc 구하기
    acc = [money[0]]
    for item in money[1:]:
        acc.append(acc[-1] + item)

    S = [0]
    # S(num) 최솟값 구하기 num은 0부터 시작하고, S(0)은 무조건 0임
    for num in range(1, N):
        min_value = float('inf')

        # num개를 선택한다고 하면, max_select 인덱스가 가장 큰 값이라고 한다
        # 2개를 선택했다고 하면 인덱스 [max_select-1], [max_select]를 선택한 것
        for max_select in range(num, N):
            # 갚아야 할 돈 pay_back_money, 실제로 빌린 돈 real_borrow_moeny
            pay_back_money = money[max_select] * (num + 1)
            real_borrow_money = acc[max_select]
            # idx 2 ~ 5 의 합을 구하고 싶으면 누적합 idx 5 에서 1까지를 빼야 함
            if max_select - num > 0:
                real_borrow_money -= acc[max_select - (num + 1)]
            # 추가적으로 내야 할 돈 extra_money의 최솟값을 구한다
            extra_money = pay_back_money - real_borrow_money
            min_value = min(min_value, extra_money)

        S.append(min_value)

    print(sum(S))
