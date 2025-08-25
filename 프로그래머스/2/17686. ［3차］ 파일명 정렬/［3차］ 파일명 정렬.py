def solution(files):
    '''
    HEAD / NUMBER / TAIL
    HEAD는 문자만
    NUMBER는 숫자(1~5개)
    TAIL은 나머지
    
    1. HAED 사전순
    2. NUMBER 숫자순 (int로)
    3. 원래 순서
    '''
    ans = []
    hnt = []
    for idx,file in enumerate(files):
        h, n = "",""
        i = 0
        while file[i].isalpha() or file[i] == " " or file[i] == "." or file[i] == "-":
            i+=1
        
        h = file[:i]
        j=i
        while j < len(file) and file[j].isdigit():
            if j-i >= 5: break
            j+=1
            # 22 23 24 25 26 27
        n = file[i:j]
        hnt.append((h, n, idx))
    hnt.sort(key = lambda x: (x[0].upper(), int(x[1]), x[2]))
    for i in hnt:
        ans.append(files[i[2]])
    return ans