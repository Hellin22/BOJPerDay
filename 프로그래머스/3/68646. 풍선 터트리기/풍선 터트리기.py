
2
3
4
5
6
7
8
9
10
11
12
13
14
def solution(a):
    answer = 1
    M = min(a)
    for _ in range(2):
        m = a[0]
        i = 1
        while m != M:
            if m >= a[i]:
                m = a[i]
                answer += 1
            i += 1
        a.reverse()
    return answer