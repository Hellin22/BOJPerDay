def solution(n, words):
    # 번호, 차례 (1번사람, 3번째)
    st = set()
    for i, word in enumerate(words): # n이 3 -> 0 1 2 / 3 4 5 / ...
        if i == 0:
            st.add(word)
        else:
            if words[i-1][-1] != word[0] or word in st: # 틀리거나 중복
                return [i % n +1, i//n + 1]
            else:
                st.add(word)
    return [0, 0]