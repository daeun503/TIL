import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

def add_two_people(target, end):
    p1, p2 = 0, end-1
    result = 0
    tmp = N
    while p1 < p2:
        hap = IN[p1] + IN[p2]
        # hap이 더 크면 줄여야 한다.
        if hap > target:
            p2 -= 1
        # hap이 더 작으면 키워야 한다.
        elif hap < target:
            p1 += 1
        # target 이면 카운트
        else:
            # p1, p2가 가리키는 값이 같을 때
            if IN[p1] == IN[p2]:
                result += p2 - p1

            # p1, p2가 가리키는 값이 다를 때
            else:
                # 이 if 문이 있어야 시간이 줄어든다
                if tmp > p2:
                    tmp = p2
                    while tmp >= 0 and IN[p2] == IN[tmp-1]:
                        tmp -= 1
                result += p2 - tmp + 1
            p1 += 1

    return result


N = int(input())
IN = sorted(list(map(int, input().split())))

# 3명 미만이면 불가
if N < 3:
    print(0)
    exit()

result = 0
for p3 in range(N-1, 1, -1):
    result += add_two_people(-IN[p3], p3)

print(result)
