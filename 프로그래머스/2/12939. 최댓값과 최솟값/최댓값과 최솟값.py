def solution(s):
    ss = s.split(" ")
    ss.sort(key = lambda x: int(x))
    return f"{ss[0]} {ss[-1]}"