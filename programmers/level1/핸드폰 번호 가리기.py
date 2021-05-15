def solution(phone_number):
    star = len(phone_number) - 4
    return '*' * star + phone_number[-4:]