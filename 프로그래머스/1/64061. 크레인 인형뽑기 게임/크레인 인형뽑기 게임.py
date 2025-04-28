'''
[[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]]

[1,5,3,5,1,2,1,4]
'''

def solution(board, moves):
    answer = 0
    
    stck = [] # stck이 있다면 stck[-1]과 비교해서 같으면 answer+=2 아니면 stck.append
    
    # moves[i]-1에 대해서 진행하기 -> j
    n = len(board) # 정사각
    for mv in moves:
        for i in range(n):
            if board[i][mv-1] != 0:
                if stck and stck[-1] == board[i][mv-1]:
                    answer+=2
                    stck.pop()
                else: stck.append(board[i][mv-1])
                
                board[i][mv-1] = 0
                break
    
    return answer