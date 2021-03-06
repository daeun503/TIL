"""
연습문제 4. 순열

4-3) 5개의 숫자 중 3자리의 순열 고르기
[1, 2, 3, 4, 5]에서 3자리의 순열을 재귀 함수를 활용하여 구현하시오.
"""
def perm(n, k, m): # n: 숫자를 결정 할 자리 인덱스, k: 순열의 길이, m: 주어진 숫자의 개수
    # 순열의 길이 = 인덱스와 동일
    # 순열의 길이와 목표 길이가 같으면 끝내기
    if k == m:
        print(sel)
    # 같지 않다면, N만큼 돌면서 방문 안한 숫자를 찾는다
    else:
        for i in range(N):
            if check[i] == 0:
                # 방문 안 한 숫자를 k자리에 넣어주고 방문표시
                sel[k] = nums[i]
                check[i] = 1
                # 재귀를 돌려주고
                perm(n, k+1, m)
                # 다음을 위해 방문 표시를 풀어준다
                check[i] = 0


nums = [1, 2, 3, 4, 5]
N = len(nums)
sel = [0]*3
check = [0]*N

perm(0, 0, 3)
