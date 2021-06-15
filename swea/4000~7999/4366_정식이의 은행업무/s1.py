import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


for tc in range(1, int(input()) + 1):
    A = list(input())
    B = list(input())
    result = 0

    for i in range(len(B)):
        Bfix1, Bfix2 = B[:], B[:]

        # B에서 한 자릿수를 바꿔주기
        if B[i] == '2':
            Bfix1[i], Bfix2[i] = '1', '0'
        elif B[i] == '1':
            Bfix1[i], Bfix2[i] = '2', '0'
        elif B[i] == '0':
            Bfix1[i], Bfix2[i] = '1', '2'

        # B 3진법 -> 10진법
        Bfix1Todec = int(''.join(Bfix1), 3)
        Bfix2Todec = int(''.join(Bfix2), 3)

        # B(10진법 -> 2진법) & A랑  xor연산 한 결과로 1의 갯수가 1개면 답
        if bin(int('0b'+''.join(A), 2) ^ Bfix1Todec)[2:].count('1') == 1:
            result = Bfix1Todec
            break
        elif bin(int('0b' + ''.join(A), 2) ^ Bfix2Todec)[2:].count('1') == 1:
            result = Bfix2Todec
            break

    print("#{} {}".format(tc, result))


