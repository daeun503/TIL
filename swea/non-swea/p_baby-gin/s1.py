# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):

run = [111, 222, 333, 444, 555, 666, 777, 888, 999]
tri = [123, 234, 345, 456, 567, 678, 789]
for tc in range(111111, 999999):
    if '0' in str(tc):
        continue
    result = 0
    # input_list = sorted(list(map(int, list(str(input())))))
    input_list = sorted(list(map(int, str(tc))))
