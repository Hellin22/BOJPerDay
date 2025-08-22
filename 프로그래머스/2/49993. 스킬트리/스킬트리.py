def solution(skill, skill_trees):
    st = set(i for i in range(26))
    for i in skill:
        st.discard(ord(i)-65)
    for i in range(len(skill_trees)):
        for k in st:
            skill_trees[i] = skill_trees[i].replace(chr(k+65), "")
    ans = 0
    st2 = set()
    for i in range(len(skill)):
        st2.add(skill[:i+1])
    for i in skill_trees:
        if i in st2: ans+=1
        if i == "": ans+=1
    return ans