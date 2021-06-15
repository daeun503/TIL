# 끝말잇기에 참여하는 사람의 수 n
def solution(n, words):
    word_dict = {}
    
    old_word = '0'
    for idx, word in enumerate(words, 0):
        if old_word[-1] == word[0] or old_word == '0' :
            word_dict[word] = word_dict.get(word, 0) + 1
            if word_dict[word] == 2:
                return [idx%n+1, idx//n+1]
        else:
            return [idx%n+1, idx//n+1]
        old_word = word
    return [0, 0]