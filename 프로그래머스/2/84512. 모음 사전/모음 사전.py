# dfs로 풀어야할듯?
'''
# 전역
str= ""
alphabets = ["A", "E", "I", "O", "U"]
dt = dict()
def 함수이름:
    for i in range(5):
        str+=alphabets[i]
        dt[str] = len(dt)+1      
        함수()
        str = str[0:len(str)-1] # 젤 뒤에꺼 빼기
'''
sttr = ""
alphabets = ["A", "E", "I", "O", "U"]
dt = dict()

def dfs():
    global sttr
    if len(sttr) == 5:
        return
    
    for i in range(5):
        sttr+=alphabets[i]
        dt[sttr] = len(dt)+1
        dfs()
        sttr = sttr[0:len(sttr)-1]

def solution(word):
    answer = 0
    dfs()
    return dt[word]
