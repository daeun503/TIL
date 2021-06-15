"""
연습 문제3. 순열 - 백트래킹
 - [1, 2, 3]의 순열 구하는 백트래킹 알고리즘을 구현하시오.
"""

# 완성된 순열 출력하는 함수
def process_solution(p, k):
    for i in range(1, k+1):
        print(data[p[i]], end=' ')
    print()


# 후보군을 생성하는 함수
def make_candidates(p, k, N, c):
    in_perm = [0] * NMAX  # 숫자를 사용했는지 여부 체크

    for i in range(1, k):
        in_perm[p[i]] = 1

    ncands = 0
    for i in range(1, N+1):
        if in_perm[i] == 0:
            c[ncands] = i
            ncands += 1


# 백트래킹을 위한 함수
def backtrack(p, k, N):
    # p: 선택한 요소의 배열 / k: 선택한 수 / N: 모든 선택의 가짓수
    c = [0] * MAXCANDIDATES    # 후보군 선택

    if k == N:                 # 순열이 완성된 경우
        process_solution(p, k) # 원하는 작업 (여기서는 순열 출력)
    else:
        # k 증가
        k += 1
        # 후보군 생성
        make_candidates(p, k, N, c)
        # 다시 backtrack
        # range 범위 잘 모르겠어서 지수님 코드 참고!
        for i in range(N-k+1): # 미선택된 것들(후보군 개수만큼, 총갯수-선택한것)
            p[k] = c[i]
            backtrack(p, k, N)


MAXCANDIDATES = 100  # 후보군 설정
NMAX = 100
p = [0] * NMAX       # 순열을 저장 할 배열
data = [0, 1, 2, 3]  # 인덱스를 편하게 사용하기 위해 0을 넣어두고 시작
backtrack(p, 0, 3)   # 3개 원소로 만드는 순열