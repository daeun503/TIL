def solution(n):
    # 2진법으로 바꿔서 1의 숫자를 센다
    target = list(str(bin(n)[2:])).count('1')
    # 1씩 증가시키면서 1의 숫자를 세서, target과 같으면 리턴
    while 1:
        n += 1
        target_n = list(str(bin(n)[2:])).count('1')
        if target_n == target:
            return n 