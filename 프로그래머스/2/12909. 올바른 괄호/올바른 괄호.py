'''
1. stck로 풀기
2. (())) -> (는 +1 )는 -1로 풀기? 음수가 되면 안됨. -> 최종적으로 0이어야
'''

def solution(s):
# 1번
    stck = []
    for i in s:
        if i == '(':
            stck.append(1)
        elif i == ')' and stck:
            stck.pop()
        else: return False
    
    if stck: return False
    else: return True
    
    
    
    

# 2번
#     num = 0
#     for i in s:
#         if i == "(":
#             num+=1
#         else:
#             if num == 0: return False
#             else: num-=1
    
#     if num != 0: return False
#     else: return True
    
