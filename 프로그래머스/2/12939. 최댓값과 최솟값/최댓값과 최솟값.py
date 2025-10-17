def solution(s):
    ss = list(map(int, s.split(" ")))
    ss.sort()
    sttr = ""
    sttr += str(ss[0])
    sttr += " "
    sttr += str(ss[-1])
    return sttr