def solution(n):
    return list(reversed([int(i) for i in str(n)]))


# 슬라이싱을 활용하는 방법이 있었네요 
def solution(n):
    return [int(i) for i in str(n)][::-1]