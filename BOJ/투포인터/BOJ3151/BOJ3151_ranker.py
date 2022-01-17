# https://blog.naver.com/PostView.naver?blogId=jinhan814&logNo=222446622366&parentCategoryNo=52&categoryNo=81&viewDate=&isShowPopularPosts=false&from=postView

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
li = list(map(int, input().split()))

dp = [0] * 40001
total = 0
for i in range(1, n):
    total += dp[20000 - li[i]]

    for j in range(i):
        dp[20000 + li[j] + li[i]] += 1

print(total)