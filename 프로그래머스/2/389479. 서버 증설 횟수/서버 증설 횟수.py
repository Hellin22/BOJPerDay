# 40분 -> 0일때 increase를 2번해서 계속 틀림
def solution(players, m, k):
    '''
    players는 동시간대 사람수 배열 [1, 2, ..., 1, 1] # 길이는 24이고 각각 0~1000명일 수 있음
    m은 서버 하나당 최대 이용자 수 -> m명이 됨 == 서버하나 추가하기 -> 네모 // m 만큼 서버가 필요
    k는 서버 운영 시간 의미  1~24
    '''    
    server_increase = 0
    server_cnt = [0] * 24 # 0~23 까지
    
    server_cnt[0] = players[0] // m
    if server_cnt[0] != 0:
        server_increase += server_cnt[0]
        for i in range(k):
            server_cnt[i] = server_cnt[0]
            
    for i in range(1, 24):
        if players[i] // m > server_cnt[i]:
            # 서버를 늘려야함. 얼마나? players[i]//m과 server_cnt[i]가 같을때 까지
            a = players[i] // m - server_cnt[i]  # a가 음수가 되면 안되지요 -> 애초에 커야지 여기 들어옴
            server_increase+=a
            for j in range(i, min(i+k, 24)):
                server_cnt[j] +=a
        
        
    return server_increase