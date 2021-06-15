import sys
sys.stdin = open('input.txt')

# stack....?
for tc in range(1, int(input())+1):
    text = input()
    store = []
    result = 0    # result = 총 잘린 조각 수
    old_t = 0     # 이전 t 값 저장
    for t in text:
        if t == "(":            # 막대면 store에 막대를 넣어준다
            store += [t]
        else:                   # 막대가 끝났거나 레이저이면
            if old_t == t:      # 막대가 끝났을 때 "))"쌍
                result += 1     # 막대 하나 끝난거니까 +1
                store.pop()     # store에 들어있던 끝난 막대 없애주기
            else:               # 레이저 일 때 "()"쌍
                store.pop()     # store에 들어있던 레이저 "("을 없애주기
                result += len(store)  # store에 들어있던 막대들 수 만큼 +
        old_t = t               # 새로운 t를 받기 위해 old_t에 t를 넣어줌

    print("#{} {}".format(tc, result))

