'''
1. stck로 풀기
2. (())) -> (는 +1 )는 -1로 풀기? 음수가 되면 안됨. -> 최종적으로 0이어야함
'''

def solution(s):
    num = 0
    for i in s:
        if i == "(":
            num+=1
        else:
            if num == 0: return False
            else: num-=1
    
    if num != 0: return False
    else: return True
    
