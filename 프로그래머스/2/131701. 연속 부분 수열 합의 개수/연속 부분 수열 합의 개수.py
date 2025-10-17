def solution(elements):
    # 누적합으로 처리
    # 1개부터 ~ 모든 ele 합 
    st = set()
    
    for i in range(1, len(elements)): # 개수
        summ = sum(elements[:i]) # 최초 합 = 개수만큼 # 0 / 0 1 / 0 1 2
        st.add(summ)
        for j in range(1, len(elements)): # 시작지점 -> 0번째 제외
            summ+= elements[(j+i-1) % len(elements)] - elements[j-1]
            st.add(summ)
    return len(st)+1