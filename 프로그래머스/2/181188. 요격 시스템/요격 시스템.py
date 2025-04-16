'''

[[1, 4], [3, 7], [4, 5], [4, 8], [5, 12], [10, 14], [11, 13]]
1 5 3 4
1.5 -> 3.5

뒤에 값이랑 앞에꺼랑 비교해서 같을때까지??
1, 4 -> 3, 7 -> 4, 5 (제일 앞에있는 뒤에값이랑 비교해야하는가?)
1, 4 3,7  이렇게 끝
4, 5 -> 4, 8 -> 5, 12 (5, 5가 나와버림 -> 5보다 작은값이 뒤에 나와야함.)

5, 12 -> 10, 14 -> 11, 13 -> 끝

'''

def solution(targets):
    answer = 0
    targets.sort()

    idx = 0
    while idx < len(targets):
        cur = targets[idx] # x, y
        answer+=1
        while True:
            # 언제 종료?
            # cur[1]이 new[0]와 같거나 더 작아지는 경우
            
            idx+=1
            if idx == len(targets): break
            new_cur = targets[idx]
            if cur[1] <= new_cur[0]:
                break
            cur[1] = min(cur[1], new_cur[1])
    
    
    return answer