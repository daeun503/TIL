import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


number = '0123456789'
for tc in range(1, 11):
    N = input()
    IN = input()

    # 중위 표현식 후위로 바꾸기 (+만 있어서 적당히..)
    postfix = IN[0]+IN[2:]+IN[1]

    # 후위 표현식 계산하기
    stack = []
    for i in postfix:
        # 만약 숫자면 stack에 쌓기
        if i in number:
            stack.append(i)
        # +면 stack에서 피연산자 두개 꺼내서 계산한 다음 다시 넣어주기
        else:
            B = stack.pop()
            A = stack.pop()
            stack.append(int(A)+int(B))

    # 마지막으로 계산된 값 스택에서 뽑아서 출력하기
    result = stack.pop()
    print("#{} {}".format(tc, result))