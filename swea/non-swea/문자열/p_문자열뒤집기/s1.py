# reversed() 직접 구현

def reverse_str(word):
    """
    word를 뒤집어 반환 - 반복문
    """
    reverse_word = ""
    for i in range(len(word)):
        reverse_word = word[i] + reverse_word
    return reverse_word

word = 'tomato'
print(reverse_str(word))