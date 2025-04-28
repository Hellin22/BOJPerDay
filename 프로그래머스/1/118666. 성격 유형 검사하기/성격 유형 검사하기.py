'''
지표 번호	성격 유형
1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)

'''
def solution(survey, choices):
    answer = ''
    list = ["R", "T", "C", "F", "J", "M", "A", "N"]
    dt = {}
    
    # 1 2 3 / 5 6 7
    for i in range(len(survey)):
        a = survey[i][0]
        b = survey[i][1]
        if choices[i] < 4: dt[a] = dt.get(a, 0) + 4-choices[i]
        else: dt[b] = dt.get(b, 0) + choices[i]-4
    
    answer += "R" if dt.get("R", 0)>=dt.get("T", 0) else "T"
    answer += "C" if dt.get("C", 0)>=dt.get("F", 0) else "F"
    answer += "J" if dt.get("J", 0) >= dt.get("M", 0) else "M"
    answer += "A" if dt.get("A", 0) >= dt.get("N", 0) else "N"
    
    return answer