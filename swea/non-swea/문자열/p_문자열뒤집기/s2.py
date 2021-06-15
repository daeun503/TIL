# reversed() 직접 구현

def reverse_str_recursion(word):
    """
    word를 뒤집어 반환 - 재귀함수
    """
    if len(word) == 1:
        return word
    else:
        return reverse_str_recursion(word[1:]) + word[0]

word = 'tomato'
print(reverse_str_recursion(word))