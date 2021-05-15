def solution(s):
    a = list(s)
    a.sort(reverse = True)
    return ''.join(a)