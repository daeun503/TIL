"""
연습 문제2. 선택 정렬 (반복 & 재귀)

선택 정렬을 반복과 재귀버전으로 구현하시오.
"""

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

# 반복(for)
def selection_sort_for(my_list):
    for i in range(0, len(my_list)-1):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

# 재귀 - 추가 파라미터 구성 가능
def selection_sort_recursion(my_list):
    # 길이가 1 이면 그냥 리턴
    if len(my_list) == 1:
        return my_list
    # 길이가 2 이상이면 최솟값 찾아서 [0]에 넣어주기 
    min_idx = 0
    for i in range(1, len(my_list)-1):
        if my_list[min_idx] > my_list[i]:
            min_idx = i
    my_list[0], my_list[min_idx] = my_list[min_idx], my_list[0]
    # [0]은 최솟값이고 나머지 뒷부분 재귀로 반복
    return [my_list[0]] + selection_sort_recursion(my_list[1:])

print(selection_sort_for(my_list))
print(selection_sort_recursion(my_list))