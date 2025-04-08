'''
6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
        x1, y1, x2, y2 (시계방향 한칸) -> 여기서  
    x2-x1, y2-y1의 최소값
    그냥 n을 x2-x1, m을 y2-y1으로 진행하기.
    그중 min을 잡고 //2 진행
    -> 가장 바깥쪽꺼만 한바퀴 돌리는구나...
    그럼 i가 0인거니까 이거에 대해서 진행하면 됨.
'''

from copy import deepcopy
from collections import deque
def rotate_arr(arr, x1, y1, x2, y2):
    dq = deque()
        
    loops = min((x2-x1), (y2-y1))//2
    # 2, 2 / 5, 4
    # 1, 1 / 4, 3
    # x1 y1  x2 y2
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    for i in range(1):
        # 위에꺼 추가 (x 고정)
        dq.extend(arr[x1-i][y1+i:y2+1-i])
        # print("위에꺼는 ", arr[x1+i][y1:y2+1-i])
        
        # 오른쪾꺼 추가 (y가 고정) == y2
        dq.extend([row[y2-i] for row in arr[x1+i+1 : x2+1-i-1]])
        # print("오른쪽 꺼는: ", [row[y2-i] for row in arr[x1+i+1 : x2+1-i-1]])
        
        # 아래쪽꺼 추가(x2로 고정 -> 뒤집기)
        dq.extend(arr[x2-i][y1+i:y2-i+1][::-1])
        # print("아래쪽 꺼는: ", arr[x2-i][y1+i:y2-i+1][::-1])
        
        
        # 왼쪽꺼 추가(y1 고정 -> 뒤집기)
        dq.extend([row[y1-i] for row in arr[x1+1+i : x2-1+1-i]][::-1])
        # print("왼쪽 꺼는: ", [row[y1-i] for row in arr[x1+1+i : x2-1+1-i]][::-1])
        
        # print(dq)
        minn = min(dq)
        
        dq.rotate(1)
        
        # 왜 new_arr이 필요한거지?
        # 위쪽
        for j in range(y1+i, y2+1-i):
            arr[x1+i][j] = dq.popleft()
        # 오른쪽
        # y2로 고정 -> y2-i
        # x1+1 ~x2-1 / x1+2 ~ x2-1-1 
        for j in range(x1+i+1, x2-i):
            arr[j][y2-i] = dq.popleft()
            
        # 아래쪽
        # x2, x2-1 / y2 ~ y1, y2-1 ~ y1+1 (이거 -1 해줘야함.)
        for j in range(y2-i, y1+i-1, -1):
            arr[x2-i][j] = dq.popleft()
        
        # 왼쪽
        # y1이 고정임. y1+i
        # x는  x2-1-i ~ <= x1+1 / x2-2 ~ <= x1+2
        for j in range(x2-1-i, x1+1+i-1, -1):
            arr[j][y1+i] = dq.popleft()

    return minn
    
def solution(rows, columns, queries):
    min_list = []
    arr = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]
    # for i in range(rows):
        # print(*arr[i])
        
    for x1, y1, x2, y2 in queries:
        minn = rotate_arr(arr, x1, y1, x2, y2)
        # for i in range(rows):
            # print(*arr[i])
        min_list.append(minn)
    return min_list
