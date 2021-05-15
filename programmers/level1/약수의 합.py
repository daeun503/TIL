# 2회차 풀이
def solution(n):
    result = n
    # 1부터 중간값 까지만. n은 초기값으로 더해주기
    for i in range(1, n//2 + 1):
        result += i if not n % i else 0
    return result