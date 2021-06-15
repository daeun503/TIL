import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

# 인덱싱
for _ in range(10):
    tc = input()
    word = input()
    txt = input()

    cnt = 0
    i = 0
    while i + len(word) <= len(txt):
        if txt[i] == word[0]:
            ok = 0
            for j in range(len(word)):
                if txt[i+j] != word[j]:
                    break
            else:
                cnt += 1
        i += 1

    print("#{} {}".format(tc, cnt))