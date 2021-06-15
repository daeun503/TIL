# 보이어 무어 알고리즘

word = 'rithm'
txt = 'a phmatalgorithmtern matching'
skip= {}

len_word = len(word)    # word의 길이
f_idx = len(word) - 1   # word의 마지막 인덱스
idx = len_word - 1      # txt에서 현재 비교하고 있는 인덱스

# 스킵 배열 생성
for i in range(len_word):
    skip[word[i]] = len_word - (i+1)


while idx <= len(txt)-1:
    # 만약 txt[idx]와 word의 마지막 글자가 동일하다면
    if txt[idx] == word[f_idx]:
        # txt[idx]앞쪽 글자들도 비교해줘야함.
        for i in range(len_word):
            # 만약 txt 앞쪽 글자가 다르면 break하고, 다음 idx로
            if txt[idx-i] != word[f_idx-i]:
                print("존재X")
                idx += len_word
                break
        # for문이 정상적으로 모두 돌았으면 존재하는 것.
        else:
            print("존재")
            break
    # 동일하지 않으면 skip 배열만큼 idx +
    else:
        idx += skip.get(txt[idx], len_word)
