def solution(n):
    answer = []
    if n == 0: return [1]
    '''
    1
    2 9
    3 10 8
    4 5 6 7
    
    1
    2 12
    3 13 11
    4 14 15 10
    5 6 7 8 9
    
    n^2 배열 초반 2번은 그냥 i+1 / j+1
    이후에는 i-1, j-1 / 만약 i-1, j-1이 0이 아니다?
    다시 i+1 / j+1
    
    사방이 0이 아니면 종료
    round = 0, 1, 2 -> round%3
    0이면 i+1 -> i가 n에 다다르거나 or i+1이 0이 아닌 경우
    1이면 j+1 -> j도 마찬가지
    2이면 i-1, j-1
    '''
    
    arr = [[0] * n for _ in range(n)]
    
    i, j = 0, 0
    mode = 0
    arr[i][j] = 1
    flg_cnt = 0
    while flg_cnt < 3:
        cur = arr[i][j]
        if mode == 0: # i+1만 진행
            if i+1 < n and arr[i+1][j] == 0: # i가 더 내려갈 수 있고 안막혀 있을때
                i+=1
                arr[i][j] = cur+1
                flg_cnt = 0
            else: 
                flg_cnt+=1
                if flg_cnt > 1: break
                mode = 1 # mode를 1로 변경
        elif mode == 1: # j 늘리기
            if j+1 < n and arr[i][j+1] == 0:
                j+=1
                arr[i][j] = cur+1
                flg_cnt = 0
            else:
                flg_cnt+=1
                mode = 2
        else:
            if i-1 >= 0 and j-1 >= 0 and arr[i-1][j-1] == 0:
                i-=1
                j-=1
                arr[i][j] = cur+1
                flg_cnt = 0
            else: 
                flg_cnt+=1
                mode = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
            else:
                break
    return answer