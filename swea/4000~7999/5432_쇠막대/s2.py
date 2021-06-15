import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    text = input()
    stack = []
    cnt = 0

    for i in text:             # input에서 한 괄호씩 가져오기
        if i == '(':           # 만약 여는 괄호면 추가하고
            stack.append(i)
        else:                  # 닫힌 괄호면 pop한다.
            stack.pop()
            # 이전 괄호가 )이면 +1만, 아니면 남은 stack의 길이를 더한다
            cnt += 1 if old_i == ')' else len(stack)
        old_i = i   # 이전 괄호가 무엇이었는지 저장한다

    print("#{} {}".format(tc, cnt))