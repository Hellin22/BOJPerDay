'''
문자열 s -> 구분된 숫자

최소 최대로 구분 (최소) (최대)
split -> 0,
'''

def solution(k):
    splited = sorted(list(map(int, k.split(' '))))
    return f"{splited[0]} {splited[-1]}" # f로 하는거 말고 다른 방법도 있는거 추가
