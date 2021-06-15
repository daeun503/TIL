def my_func(idx, sel, numbers, target):
    global result
    # 종료 조건 : sel을 모두 다 채우고, 그 값에 target이면 +1
    if idx == len(numbers):
        if sum(sel) == target:
            result += 1
        return
    
    # 백트래킹
    sel[idx] = numbers[idx]
    my_func(idx + 1, sel, numbers, target)
    sel[idx] = -numbers[idx]
    my_func(idx + 1, sel, numbers, target)

def solution(numbers, target):
    global result
    N = len(numbers)
    sel = [0] * N
    result = 0
    my_func(0, sel, numbers, target)
    return result