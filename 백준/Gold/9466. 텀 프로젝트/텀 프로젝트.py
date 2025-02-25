import sys
from collections import deque
inp = sys.stdin.readline

t = int(inp().strip())
for _ in range(t):
    n = int(inp().strip())

    from_to = [0] + list(map(int, inp().strip().split()))
    arr = [0] * (n+1) # 순환 or not 확인 문제
    
    res = 0
    for i in range(1, n+1):
        st1 = set()
        st2 = set()
        cur = i
        if arr[i] == 0: st1.add(i) # i번째 정점부터 시작
        while arr[from_to[cur]] == 0:
            if from_to[cur] not in st1 and from_to[cur] not in st2:
                st1.add(from_to[cur])
                # cur = arr[cur]
            elif from_to[cur] in st1: # st1에만 존재
                st1.remove(from_to[cur])
                st2.add(from_to[cur])
                # cur = arr[cur]
            elif from_to[cur] in st2:
                break
            # elif arr[cur] in st2: 
                # cur = arr[cur]
            cur = from_to[cur]
            # 언제까지 반복해야하는가? # st2에 있는게 하ㅏㄴ번더 나온다면?
        # st2 -> 1로, st1 -> -1로
        for val in st1:
            arr[val] = -1
        for val in st2:
            arr[val] = 1
        # print(arr)
        if arr[i] == -1: res+=1
    print(res)