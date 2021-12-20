import sys
sys.stdin = open("input.txt", "r")

stick = int(input())


###########################

# while문 안은 k 6 ~ 0까지
k, result = 7, 0
while k:
    k -= 1
    if stick & (1 << k):
        result += 1

print(result)

############################
# 한 줄로
# print(bin(stick).count("1"))
