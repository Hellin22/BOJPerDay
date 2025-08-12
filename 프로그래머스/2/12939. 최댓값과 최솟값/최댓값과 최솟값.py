'''
문자열 s -> 구분된 숫자들

최소 최대로 구분 (최소) (최대)
split -> 0, -1
'''

def solution(k):
    splited = sorted(list(map(int, k.split(' '))))
    return f"{splited[0]} {splited[-1]}"
