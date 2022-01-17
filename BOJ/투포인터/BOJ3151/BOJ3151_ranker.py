# https://blog.naver.com/PostView.naver?blogId=jinhan814&logNo=222446622366&parentCategoryNo=52&categoryNo=81&viewDate=&isShowPopularPosts=false&from=postView

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 40001
total = 0

# 배열의 인덱스가 음수가 되지 않도록 적당한 숫자 20000를 더해준다.
for i in range(n):
    total += dp[20000 - arr[i]]

    for j in range(i):
        dp[20000 + arr[j] + arr[i]] += 1

print(total)
