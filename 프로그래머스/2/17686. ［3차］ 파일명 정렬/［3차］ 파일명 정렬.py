'''
["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")
1. HEAD 부분을 기준으로 사전 순 (대소문자 구분x)
2. NUMBER의 숫자 순으로 정렬한다. 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬 (0 무시됨.)
-> int 적용하면됨
3.  원래 입력에 주어진 순서를 유지한다.

자 그러면 1. HEAD, NUMBER를 각각 구한다.
2. HEAD기준(대소문자 구분X -> 모두 소문자로), NUMBER를 (int 적용해서 하기)
즉, (소문자 HEAD, int(NUMBER), idx) -> idx는 정렬이 바꾸면 안되기 때문임.

'''


def solution(files):
    answer = []
    heads = []
    numbers = []
    
    def headFind(sttr):
        for i in range(len(sttr)):
            if 48 <= ord(sttr[i]) <= 57: return i
    
    def numberFind(sttr):
        for i in range(len(sttr)):
            if 48 <= ord(sttr[i]) <= 57: continue
            else: return i 
    
    for i in range(len(files)): # 모든 파일에 대해서. file = foo9.txt
        file = files[i] 
        
        headIdx = headFind(file) # 뭘 넣어줘야할까? 
        heads.append(file[:headIdx])
        file = file[headIdx:]
        numberIdx = numberFind(file) # 48 57
        numbers.append(int(file[:numberIdx]))
    headNumberIdx = []
    
    for idx in range(len(files)):
        headNumberIdx.append((heads[idx].lower(), numbers[idx], idx))
    headNumberIdx.sort()

    for i in range(len(headNumberIdx)):
        answer.append(files[headNumberIdx[i][2]])
    return answer
