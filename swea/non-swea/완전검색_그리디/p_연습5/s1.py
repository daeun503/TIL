"""
연습문제 4. 부분 집합의 합 구현

4-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""

def powerset(idx):
    if idx == N:
        result = 0
        for a, b in zip(nums, sel):
            result += a*b
        print("부분 집합 위치는 {}이고, 합은 {}".format(sel, result))
    else:
        sel[idx] = 0      # idx위치 부분집합 체크 X
        powerset(idx+1)   # idx+1 위치 체크하러
        sel[idx] = 1      # idx위치 부분집합 체크 O
        powerset(idx+1)   # idx+1 위치 체크하러

nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
sel = [0] * N
powerset(0)