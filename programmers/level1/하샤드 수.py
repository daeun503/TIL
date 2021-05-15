def solution(x):
     return False if (x / sum(map(int, str(x)))) % 1 else True
     # return not bool(x / sum(map(int, str(x))) % 1)
     # return (x / sum(map(int, str(x))) % 1) == 0