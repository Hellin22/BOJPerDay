'''
시간에 대해서 이분탐색
-> 최소는 1, 
'''

def solution(n, times):
    answer = 10000000000000000001# 최대값.
    r, l = max(times)*n, min(times)
    while r >= l:
        mid = (r+l)//2
        pn = 0
        for t in times:
            pn += mid // t
        if pn < n: # 사람 다 못채움 -> 시간 늘리기
            l = mid+1
        else: # 사람 다 채움
            answer = min(answer, mid)
            r = mid-1
    return answer