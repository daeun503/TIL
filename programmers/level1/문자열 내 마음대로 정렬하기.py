# 앞에 기준 단어를 추가하여 "기준 단어+원래 단어" 형태로 만든다.
# 그러면 기준 단어를 기준으로 sort하게 되며, 기준 단어가 같으면 원래 단어 기준으로 sort하게 된다.
# 리턴 할 때는 기준 단어 떼고 리턴 [1:]

def solution(words, n):   
    # 앞에 기준 단어를 추가하여 "기준 단어+원래 단어" 형태로 만든다.
    # 그러면 기준 단어를 기준으로 sort하게 되며, 기준 단어가 같으면 원래 단어 기준으로 sort하게 된다.
    sort_words = [word[n]+word for word in words]
    sort_words.sort()
    return [sort_word[1:] for sort_word in sort_words]