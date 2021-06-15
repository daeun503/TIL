def solution(s):
    cnt, cnt_0 = 0, 0
    while s != "1":
        cnt += 1
        cnt_0 += s.count('0')
        s = bin(s.count('1'))[2:]
    return [cnt, cnt_0]