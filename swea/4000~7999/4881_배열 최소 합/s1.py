import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# 코드를 통째로 외우고 있다;
def my_func2(pick, my_sum):
    global result
    r = len(pick)

    # 종료조건
    if r == N:
        if my_sum < result:
           result = my_sum
        return

    # 유망성 검사
    if my_sum > result:
        return

    # 백트래킹
    for c in range(N):
        if c not in pick:
            my_func(pick+[c], my_sum + IN[r][c])

# 방문 체크로 다시 풀어보기
def my_func(pick, my_sum, visited):
    global result

    # 종료조건
    if len(pick) == N:
        if my_sum < result:
           result = my_sum
        return

    # 유망성 검사
    if my_sum > result:
        return

    # 백트래킹
    for c in range(N):
        if visited[c] == 0:
            visited[c] = 1
            my_func(pick+[c], my_sum + IN[len(pick)][c], visited)
            visited[c] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    result = 999999
    # my_func2([], 0)
    my_func([], 0, [0] * N)
    print("#{} {}".format(tc, result))

'''
배열 최소합
- 전에 풀었을 때는 못 풀었었다. 그 때 백트래킹으로 힘들었어서 이 문제를 열심히 연구했던 기억이 난다.
- 그래서 이번에 풀 때 완전 똑같이 풀었다. 통째로 외우고 있어서 5분만에 뚝딱 작성했다;;
- 새롭게 방문 체크로도 풀어봤다. 이렇게 푸는게 맞는가? 싶지만 풀리긴 했다. 근데 기존 방법이 더 좋아보인다.
- 약간 새로운 방법으로도 혼자 풀 수 있으니까 이제 백트래킹에 꽤 익숙해진게 아닐까?하고... 행복회로...
'''
