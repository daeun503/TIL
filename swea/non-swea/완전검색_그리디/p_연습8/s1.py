"""
연습문제 5. 조합

5-2). nCr에서 r이 변화하는 경우 -> 재귀 활용
"""

def comb(n, s, N, r):
    """
    n: c[n]에서 채울 인덱스 -> 조합의 인덱스
    s: 선택 구간의 시작점
    N: 전체 범위(주어진 개수)
    r: 조합으로 고를 개수
    """
    # n이 r과 같아지면 리턴해서 n이 r보다 커질때는 안보도록
    if n == r:
        print(check)
        return
    else:
        for i in range(s, len(nums)):
            check[n] = nums[i]         # 인덱스 n에 값 써주기
            # 인덱스 n+1에 값 써넣으러 & 범위는 i+1부터 찾기
            comb(n + 1, i + 1, N, r)

# 10개 중 3개 고르기
N = 10
r = 3

# 숫자 목록
nums = [1, 2, 3, 4, 5, 6]

# 채울 자리 == 선택 할 자리
check = [0] * r

# comb(check에서 몇 번째 자리를 고를 것인가,  채울 인덱스, 전체 N, r개를 고르기)
comb(0, 0, N, r)
