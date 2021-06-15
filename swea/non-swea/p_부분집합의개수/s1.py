# # 6개의 원소가 담긴 리스트
# nums = [3, 6, 7, 1, 5, 4]
# # 리스트의 크기
# n = len(nums)
# # 부분집합의 개수를 더해 갈 변수
# cnt = 0
#
# for i in range(1 << n):
#     cnt += 1
#     for j in range(n):
#         if i & (1 << j):
#             print(nums[j], end = ' ')
#     print()
# print(cnt)




nums = "abc"
n = len(nums)
for i in range(1 << n):
    tmp = ''
    for j in range(n):
        if i & (1 << j):
            tmp += nums[j]
    print(tmp)