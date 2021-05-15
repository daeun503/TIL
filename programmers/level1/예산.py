def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)


# 매번 sum해주기 싫으면 이거
def solution(d, budget):
    d.sort()
    hap = sum(d)
    while hap > budget:
        hap -= d.pop()
    return len(d)