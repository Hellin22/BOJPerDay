'''
n명의 학생 -> lost는 잃어버린 학생 번호임. + reserve는 여벌임.
lost는 -1이 되고 reserve 학생들은 +=1로 진행?
n명 돌면서 0이면 넘어가기
아니다? 왼쪽꺼 빌리기 -> 못빌리면 오른쪽꺼 빌리기
왼쪽꺼 다 하고나서 오른쪽으로 진행하기
'''


def solution(n, lost, reserve):
    answer = 0
    
    cloth_cnt = [0] * n
    for idx in lost:
        cloth_cnt[idx-1] = -1
    
    for idx in reserve:
        cloth_cnt[idx-1]+=1
    
    for i in range(n):
        if cloth_cnt[i] == -1:
            if i == 0:
                if cloth_cnt[1] == 1:
                    cloth_cnt[0], cloth_cnt[1] = 0, 0
            elif i == n-1:
                if cloth_cnt[i-1] == 1:
                    cloth_cnt[i], cloth_cnt[i-1] = 0, 0
            else:
                if cloth_cnt[i-1] == 1:
                    cloth_cnt[i], cloth_cnt[i-1] = 0, 0
                    continue
                elif cloth_cnt[i+1] == 1:
                    cloth_cnt[i], cloth_cnt[i+1] = 0, 0
                    
    
    
#     # 1. 본인 왼쪽꺼를 확인하기
#     for i in range(1, n):
#         if cloth_cnt[i] == -1: 
#             if cloth_cnt[i-1] == 1:
#                 cloth_cnt[i], cloth_cnt[i-1] = 0, 0
    
#     for i in range(0, n-1):
#         if cloth_cnt[i] == -1: 
#             if cloth_cnt[i+1] == 1:
#                 cloth_cnt[i], cloth_cnt[i+1] = 0, 0
        
    for i in range(0, n):
        if cloth_cnt[i] != -1:
            answer+=1
    return answer