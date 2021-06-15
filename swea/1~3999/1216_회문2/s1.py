import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 박스에서 text문자열 한 줄씩 꺼내서 비교할 것
# 현재 회문이 몇 자인지 세는 count
# box : ['sdfsfs', 'sdfsfs', 'sdfsfs']
# CBAABCCACBCACCCBBAAA
def my_func(box):
    cnt_list = []
    for text in box:
        i = 0
        palindrome_cnt = 0
        store = []
        tmp = []
        while i < len(text):
            if tmp[-1:] == [text[i]] and palindrome_cnt == 0:  # 짝수 스타트 부분
                old_start = i
                store += [tmp.pop()]
                store += [text[i]]
                palindrome_cnt += 2

            elif tmp[-2:-1] == [text[i]] and palindrome_cnt == 0:  # 홀수 스타트 부분
                old_start = i
                b = [tmp.pop()]
                store += [tmp.pop()]
                store += b
                store += [text[i]]
                palindrome_cnt += 3

            elif tmp[-1:] == [text[i]]:                          # 짝이 있는 경우
                store = [tmp.pop()] + store
                store += [text[i]]
                palindrome_cnt += 2

            else:
                if palindrome_cnt:
                    cnt_list.append(palindrome_cnt)
                    i = old_start
                    tmp += store
                else:
                    tmp += store
                    tmp += [text[i]]
                store = []
                palindrome_cnt = 0
            if i == len(text)-1 :
                cnt_list.append(palindrome_cnt)
            i += 1

    return max(cnt_list)


for _ in range(1, 2):
    tc = int(input())
    cnt = 0
    box = [input() for _ in range(100)]  # 정방향
    rotated_box = [''.join(char) for char in list(zip(*box))]  # 시계 방향으로 90도 회전

    a = my_func(box)
    b = my_func(rotated_box)

    print("#{} {}".format(tc, max(a, b)))
