"""
연습문제 4. 부분 집합의 합 구현

4-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기

** 비트 연산
- 원소 수에 해당하는 N개의 비트열을 활용
- n번째 비트값이 1이면 n번째 원소가 '포함'되었음을 의미

0   0 0 0 0   {A, B, C, D}
1   0 0 0 1   {A}
2   0 0 1 0   {B}
3   0 0 1 1   {B, A}
...........
14  1 1 1 0   {D, C, B}
15  1 1 1 1   {D, C, B, A}
"""

#1. 재귀 활용
def powerset(idx):
    if idx == N:
        result = [ a*b for a, b in zip(nums, sel) if a*b ]
        if sum(result) == 0:
            print("sel:{}, 합:{}, 부분집합:{}".format(sel, sum(result), result))
    else:
        sel[idx] = 0      # idx위치 부분집합 체크 X
        powerset(idx+1)   # idx+1 위치 체크하러
        sel[idx] = 1      # idx위치 부분집합 체크 O
        powerset(idx+1)   # idx+1 위치 체크하러

nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
sel = [0] * N
powerset(0)
print('------------------------------------')


#2. 비트 연산 활용
def bit_powerset():
    for i in range(1 << N):
        hap = 0
        powerset = []
        for j in range(N):
            if i & (1 << j):
                hap += nums[j]
                powerset.append(nums[j])
        if hap == 0:
            print("합:{}, 부분집합:{}".format(hap, powerset))

nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
bit_powerset()