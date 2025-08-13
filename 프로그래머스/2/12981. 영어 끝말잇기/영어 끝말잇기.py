def solution(n, words):
    st = set()
    for i, word in enumerate(words):
        if (i != 0 and words[i-1][-1] != words[i][0]) or word in st or len(word) == 1: # 실패
            return [i%n+1, i//n+1]
        st.add(word)
    return [0, 0]
    
    '''
    n명 끝말잇기 -> 1 ~ n번
    
    순환 구조 + 앞선사람의 마지막 문자로 시작 + 이전 단어 사용 안됨 + 한글자 안됨
    
    가장 먼저 탈락하는 사람 번호 + 몇번째 차례에 탈락?
    '''