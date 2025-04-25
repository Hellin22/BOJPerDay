'''
"2022.05.19"	
["A 6", "B 12", "C 3"]	
["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

달 수로 주어짐 1~100
그러면 일은 그대로
현재 "달"에 A의 유효기간을 더함.
% 13을 해야하나?
5+7 %12 -> 0
1 1
2 2
12 12
13 1
달 + 유효기간 -1 %12 -> 11%12 -> 11+1 == 12
13-1%12 = 0 -> 1

'''
def solution(today, terms, privacies):
    answer = []
    dt = dict()
    y, m, d = today.split(".")
    for ter in terms: 
        a, b = ter.split(" ")
        dt[a] = int(b)
    
    for i, pri in enumerate(privacies):
        date, a = pri.split(" ")
        year, month, day = map(int, date.split("."))
        
        di, mo = divmod(month+dt[a]-1, 12)

        # 조건은
        # 년도가 더 작으면 바로
        # 년도가 크면 아님
        # 년도가 같다면 month 보기
        if year+di < int(y): # 현재 년도가(유효기간)이 더 작음 -> 바로 추가
            answer.append(i+1)
        elif year+di > int(y): continue
        else: # 2개가 동일하다면
            if mo+1 < int(m):
                answer.append(i+1)
            elif mo+1 > int(m): continue
            else:
                if day <= int(d): answer.append(i+1)
        
    return answer