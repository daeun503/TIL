import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N, IN = input().split()
    N = int(N)
    IN = list(IN)
    IN_R = []

    while IN:
        # print(IN, IN_R, '//', IN[-1:], IN_R[:1])
        # 연속 같은게 있으면 IN의 마지막 요소, IN_R의 첫번째 요소 제거
        if IN[-1:] == IN_R[:1]:   IN_R = IN_R[1:]
        # 연속 같은게 없으면 IN의 마지막 요소를 IN_R에 붙여준다.
        elif IN[-1:] != IN_R[:1]: IN_R = IN[-1:] + IN_R
        # 위에서 언급한 IN은 마지막 요소 하나 떼주는 코드
        IN = IN[:-1]

    result = IN + IN_R
    print("#{} {}".format(tc, ''.join(result)))