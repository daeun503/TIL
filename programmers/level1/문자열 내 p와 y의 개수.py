def solution(s):
    p_count = list(s).count('p') + list(s).count('P')
    y_count = list(s).count('y') + list(s).count('Y')
    return True if p_count == y_count else False