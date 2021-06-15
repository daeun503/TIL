import sys
sys.stdin = open("input.txt", "r")
# sys.stdin = open("input2.txt", "r")
from pandas import DataFrame

T = int(input())

problem = [list(map(int, input().split())) for _ in range(9)]
problem_col = [list(i) for i in zip(*problem)]
print(DataFrame(problem))


#
#
# text = [input() for _ in range(5)]
# text_col = [''.join(text) for i in zip(*text)]