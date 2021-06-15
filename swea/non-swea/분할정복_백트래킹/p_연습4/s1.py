"""
연습 문제4. 이진 탐색
 - 이진 탐색을 반복문과 재귀 함수를 활용하여 구현하시오.
 - 찾고자 하는 값(target)이 있다면 해당 값의 인덱스를 없다면 -1을 반환하시오.

중요!
"""

#1. iteration
def binary_search_iteration(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
# target = 90    # 없는 경우 -> -1
print(binary_search_iteration(nums, target))

#2. recursion
def binary_search_recursion(nums, low, high, target):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return binary_search_recursion(nums, low, mid-1, target)
        else:
            return binary_search_recursion(nums, mid+1, high, target)

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
# target = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
target = 90    # 없는 경우 -> -1
print(binary_search_recursion(nums, 0, len(nums)-1, target))