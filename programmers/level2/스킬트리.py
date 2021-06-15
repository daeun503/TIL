# 1회차
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:           # 입력받은 skill_trees에서 하나씩 확인
        necessary_skill_tree = skill_tree    # skill_tree를 필수 스킬트리에 복사해서 변형할 것
        for word in skill_tree:              # 확인하고 있는 스킬 트리에서 word를 하나씩 확인
            if not word in skill:            # 만약 스킬에 word가 없으면 해당 word 삭제해 줌
                necessary_skill_tree = necessary_skill_tree.replace(word,'')
        if skill[:len(necessary_skill_tree)] == necessary_skill_tree:
            answer += 1                      # 필요없는거 다 뺐을 때 서로 동일하면 가능한 스킬트리
    return answer