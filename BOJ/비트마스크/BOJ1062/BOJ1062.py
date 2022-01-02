import sys
sys.stdin = open("input.txt", "r")
from itertools import combinations


def func():
    result = 0
    flag = 0
    for additional in combinations(candidiate, K - 5):
        flag = 1
        # 가르치는 알파벳 : 필수 + 추가
        teaching_words = 0
        for w in (necessary | set(additional)):
            teaching_words |= (1 << (ord(w) - ord('a')))

        # 해당 알파벳으로 알 수 있는 단어 수 세기
        count = 0
        for word in bin_word:
            if teaching_words == (teaching_words | word):
                count += 1

        # result 와 count 중 더 높은 숫자로 갱신
        result = max(result, count)
    
    # candidiate 나 flag가 0이면 모든 단어를 배울 수 있음 (예외 처리)
    if not flag or not candidiate:
        result = N

    return result


N, K = map(int, input().split())
bin_word = [0] * N
necessary = {"a", "n", "t", "i", "c"}
candidiate = set()

if K < 5:
    print("0")
elif K == 26:
    print(N)
else:
    for i in range(N):
        # 단어를 bin 형식으로 바꿔주기
        word = input()
        for w in word:
            bin_word[i] |= (1 << (ord(w) - ord('a')))

        # 알파벳들을 후보군에 넗기
        candidiate |= set(list(word))
    # 필수는 따로 처리할거라, 제외시키기
    candidiate -= necessary
    print(func())
    
    
################################################################
# candidiate를 bdefghjklmopqrsuvwxyz로 두고 하는 방법

# def func():
#     result = 0
#     for additional in combinations(candidiate, K - 5):
#         # 가르치는 알파벳 : 필수 + 추가
#         teaching_words = 0
#         for w in (necessary | set(additional)):
#             teaching_words |= (1 << (ord(w) - ord('a')))
# 
#         # 해당 알파벳으로 알 수 있는 단어 수 세기
#         count = 0
#         for word in bin_word:
#             if teaching_words == (teaching_words | word):
#                 count += 1
# 
#         # result 와 count 중 더 높은 숫자로 갱신
#         result = max(result, count)
# 
#     return result
# 
# 
# N, K = map(int, input().split())
# bin_word = [0] * N
# necessary = {"a", "n", "t", "i", "c"}
# candidiate = "bdefghjklmopqrsuvwxyz"
# 
# if K < 5:
#     print("0")
# elif K == 26:
#     print(N)
# else:
#     for i in range(N):
#         # 단어를 bin 형식으로 바꿔주기
#         word = input()
#         for w in word:
#             bin_word[i] |= (1 << (ord(w) - ord('a')))
#     print(func())
