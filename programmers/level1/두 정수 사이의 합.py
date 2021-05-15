# a, b 대소 비교해서 a가 더 크면 자리 바꿔준 후 sum

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a,b+1))