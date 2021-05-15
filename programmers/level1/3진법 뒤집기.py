# 1. 10진법 -> 3진법으로 바꾸기
# 2. 뒤집지말고 그냥 인덱스 0 부터 1, 3, 9 .. 곱해서 10진법으로 바꿔주기

def solution(n):
    answer = 0
    number = to10_3(n)
    for i in range(len(number)):
        answer += int(number[i]) * (3 ** i)
    return answer

def to10_3(n):
    if n // 3 == 0:
        return f'{n%3}'
    else:
        return to10_3(n//3) + f'{n%3}'