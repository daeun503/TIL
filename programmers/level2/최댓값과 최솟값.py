def solution(s):
    s_list = list(map(int, s.split()))
    min_s = min(s_list)
    max_s = max(s_list)
    return str(min_s)+' '+str(max_s)