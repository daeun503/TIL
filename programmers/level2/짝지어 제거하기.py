def solution(s):
    s = list(s)
    stack = [s.pop()]
    while s:
        stack.append(s.pop())
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return 0 if stack else 1