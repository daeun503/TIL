import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())
IN = sorted(list(map(int, input().split())))

# result 에 너무 작은 값으로 초기화해서 틀렸었음
s, e = 0, N-1
result = float('inf')

# O(n^3) s, e 모든 경우의 수 정해주기
for s in range(N-3):
    for e in range(N-1, s+2, -1):
        people1 = IN[s] + IN[e]

        ss, ee = s + 1, e - 1
        while ss < ee:
            # 높이 차로 갱신
            people2 = IN[ss] + IN[ee]
            result = min(result, abs(people1 - people2))
            # people1이 더 크다면 ss + 1
            if people1 > people2:
                ss += 1
            # people1이 더 작다면 ee - 1
            elif people1 < people2:
                ee -= 1
            # people1과 같다면 종료
            else:
                result = 0
                print(0)
                exit()

print(result)

