def solution(s):
    answer = 0
    stck = []
    cur = 0
    for _ in range(len(s)):
        stck.clear()
        flag = True
        for i in range(len(s)):
            if s[(cur+i) % len(s)] in "[({":
                stck.append(s[(cur+i) % len(s)])
            elif s[(cur+i) % len(s)] == "]":
                if stck and stck[-1] == "[":
                    stck.pop()
                else: 
                    flag = False
                    break
            elif s[(cur+i) % len(s)] == ")":
                if stck and stck[-1] == "(":
                    stck.pop()
                else: 
                    flag = False
                    break
            elif s[(cur+i) % len(s)] == "}":
                if stck and stck[-1] == "{":
                    stck.pop()
                else: 
                    flag = False
                    break
        if flag and not stck: 
            answer+=1 
        cur+=1
            
            
            
    return answer