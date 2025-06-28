'''
최후에 남길 수 있는 풍선 구하기
'''


def solution(a):
    answer = 2
    n = len(a)
    if n == 1: return 1
    elif n == 2: return 2

    left, right = [1000000001] * n, [1000000001] * n
    
    for i in range(1, n-1):
        left[i] = min(left[i-1], a[i-1])
    
    for i in range(n-2, 0, -1):
        right[i] = min(right[i+1], a[i+1])
    
    for i in range(1, n-1):
        # left[i]는 i번째 일때 왼쪽의 max, right[i]는 i번째 일때 오른쪽의 max
        if max(left[i], right[i], a[i]) != a[i]: answer+=1
    return answer