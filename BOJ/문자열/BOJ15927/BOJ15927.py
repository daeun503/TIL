import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


IN = input()

# 글자가 모두 한 단어면 -1
if len(set(IN)) == 1:
    print(-1)
# 펠린드롬일 때 한 글자만 빼면 무조건 펠린드롬이 아님
elif IN == IN[::-1]:
    print(len(IN) - 1)
# 펠린드롬이 아니면 길이 출력
else:
    print(len(IN))


######################################
# 시간 초과

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

IN = input()
result, s = 0, 0
length = len(IN)

while s < length - result:
    # 두 단어 이상이면 펠린드롬 체크
    e = length
    for e in range(length, s + result, -1):
        if e - s < 2:
            break
        # 펠린드롬이 아니면 최장 길이 갱신
        if not is_palindrome(IN[s:e]):
            result = e - s
            break
    s += 1

if not result:
    print(-1)
else:
    print(result)


