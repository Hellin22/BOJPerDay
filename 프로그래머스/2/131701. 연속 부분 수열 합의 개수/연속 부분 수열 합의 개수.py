def solution(elements):

    st = set()
    n = len(elements)
    for i in range(0, n): # 몇개의 원소를 가진 부분수열인지
        l, r = 0, i
        wd = sum(elements[l:r+1])
        st.add(wd)
        for j in range(1, n):
            wd-=elements[l]
            l, r = (l+1) % n, (r+1) % n
            wd+=elements[r]
            st.add(wd)
    
    return len(st)

    '''
    연속하는 부분수열의 합으로 만들 수 있는 수
    저장은 set
    len(elements)까지 반복
    1개 ~ n-1개 까지 -> return ans + 1
    윈도우 슬라이싱으로 진행 -> left, right -> 둘다 +1 % n
    초기값(몇개를 연속으로 더하느냐)이 중요한듯? left가 다시 0이 되면 종료
    '''
    
    