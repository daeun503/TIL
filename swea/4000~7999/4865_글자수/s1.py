import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    my_dict = {}

    for i in str1:                     # str1에 있는 값들을 key로 하는 dict
        if not my_dict.get(i, 0):      # 만약 my_dict[i]가 비어있으면 (단어 한 번만 세기위해)
            my_dict[i] = str2.count(i) # str2에서 세서 value에 넣기

    print("#{} {}".format(tc, max(my_dict.values())))

    max_word = [key for key, value in my_dict.items() if value == max(my_dict.values())]