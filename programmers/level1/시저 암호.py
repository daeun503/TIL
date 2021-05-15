def solution(word, n):
    result = ''      # A 가 65 Z가 90, a가 97 z가 122=> 32 차이

    for i in word:
        if i == ' ':
            result += ' '
        elif ord(i) >= 97:           # 소문자 이면
            if ord(i) + n > 122:     # 소문자 z 초과하면
                result += chr(ord(i) + n - 26)
            else:
                result += chr(ord(i) + n)
        else:                        # 대문자 이면
            if ord(i) + n > 90:      # 대문자 Z 초과하면
                result += chr(ord(i) + n - 26)
            else:
                result += chr(ord(i) + n)

    return result