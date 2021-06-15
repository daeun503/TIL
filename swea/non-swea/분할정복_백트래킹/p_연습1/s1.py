"""
연습 문제1. 정렬 복습 - 정렬1
"""
#1. 버블 정렬
def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(bubble_sort(bubble_nums))

#2. 선택 정렬
def selection_sort(nums):
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(selection_sort(selection_nums))

#3. 카운팅 정렬
def couting_sort(nums):
    # 카운팅 정렬 만들어주기
    C = [0] * (max(nums) + 1)
    for i in range(len(nums)):
        C[nums[i]] += 1
    # 카운팅 정렬의 다음 인덱스 벨류는 이전 벨류 + 현재 벨류
    for j in range(1, len(C)):
        C[j] += C[j-1]
    # 정렬시키기. nums에서 읽어서 삽입할 때마다 C는 하나씩 깎아줌
    result = [0] * len(nums)
    for k in range(len(nums)-1, -1, -1):
        result[C[nums[k]]-1] = nums[k]
        C[nums[k]] -= -1
    return result

counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(couting_sort(counting_nums))