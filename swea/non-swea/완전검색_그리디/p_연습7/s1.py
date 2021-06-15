"""
연습문제 5. 조합

5-1). nCr에서 r이 고정인 경우 -> for활용

5개의 숫자에서 3개를 선택하는 조합
6개의 숫자에서 3개를 선택하는 조합
....
 -> nCr에서 n의 개수는 가변적이지만 r의 개수가 고정된 경우에 활용

M개에서 3개를 고르는 경우
인덱스          M-3  M-2  M-1
      0    1    2    3    4
"""

nums = [1, 2, 3, 4, 5]
M = len(nums)

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            print(nums[i], nums[j], nums[k])