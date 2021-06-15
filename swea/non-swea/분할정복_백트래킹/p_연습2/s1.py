"""
연습 문제2. 부분집합 - 백트래킹
 - {1, 2, 3}의 부분집합을 구하는 백트래킹 알고리즘을 구현하시오.
"""

# 완성된 부분집합을 출력하는 함수
def process_solution(s, k):
    for i in range(1, k+1):
        if s[i] == 1:
            print(data[i], end=' ')
    print()


# 후보군을 생성하는 함수
def make_candidates(c):
    # 부분집합: 포함 / 미포함 -> 2가지
    # 후보를 선택하는 c 배열은 호출 될 때마다 매번 새로 생성
    c[0] = 1
    c[1] = 0


# 백트래킹을 위한 함수
def backtrack(s, k, N):
    c = [0] * MAXCANDIDATES    # 후보군 선택

    if k == N:                 # 순열이 완성된 경우
        process_solution(s, k) # 원하는 작업 (여기서는 부분집합 출력)
    else:
        # k 증가
        k += 1
        # 후보군 생성
        make_candidates(c)
        # 다시 backtrack
        # ncands = 2 고정
        for i in range(2):
            s[k] = c[i]
            backtrack(s, k, N)


MAXCANDIDATES = 100  # 후보군 설정
NMAX = 100
s = [0] * NMAX       # 부분집합을 저장 할 배열
data = [0, 1, 2, 3]  # 인덱스를 편하게 사용하기 위해 0을 넣어두고 시작
backtrack(s, 0, 3)   # 3개의 원소를 갖는 부분집합