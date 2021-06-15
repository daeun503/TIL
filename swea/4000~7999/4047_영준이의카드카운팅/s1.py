import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def my_card(IN):
    # 지금 가지고 있는 카드 세기
    for i in range(0, len(IN), 3):
        card[IN[i]][int(IN[i + 1:i + 3])] += 1

    # 부족한 카드 계산.
    result = [13, 13, 13, 13]
    for idx, i in enumerate(['S', 'D', 'H', 'C']):
        for j in card[i]:  # card[i] 는 [0] * 14 인 리스트.
            if j > 1 :
                return 'ERROR'
        # card[i]의 요소에 1이상인 값이 없을 때
        result[idx] -= sum(card[i])
    return result


T = int(input())
for tc in range(1, T + 1):
    IN = input()
    card = {'S': [0] * 14, 'D': [0] * 14, 'H': [0] * 14, 'C': [0] * 14}
    result = my_card(IN)
    # 출력
    if result == 'ERROR':
        print("#{} ERROR".format(tc))
    else:
        print("#{}".format(tc), *result)

