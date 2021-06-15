import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    # N자리 16진수 IN
    # ex) 4 47FE
    N, IN = input().split()

    # int(x, base) : base진법으로 표기된 x를 10진법 값으로 돌려준다.
    # bin(0b...), oct(0o...), hex(0x...)
    result = ''
    for i in IN:
        tmp = str(bin(int(i, 16))[2:])
        result += '0'*(4-len(tmp)) + tmp
        print('{}는 2진수로 {}이고 지금까지 누적 {}'.format(i, tmp, result))

    print("#{} {}".format(tc, result))
    print()