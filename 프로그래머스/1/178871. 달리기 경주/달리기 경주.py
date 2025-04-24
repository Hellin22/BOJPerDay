'''
자기 바로 앞의 선수 추월할 때, 추월한 선수의 이름을 부름
mumu", "soe", "poe

["mumu", "soe", "poe", "kai", "mine"]

["kai", "kai", "mine", "mine"]

["mumu", "kai", "mine", "soe", "poe"]

1. players 리스트
2. dt[players[i]] = i
3. dt[i] = players[i]

'''

def solution(players, callings):
    answer = []
    dt = dict()
    for i, player in enumerate(players):
        dt[player] = i
        dt[i] = players[i]
    
    
    for player in callings:
        # player가 추월
        
        # 현재 플레이어
        ci = dt[player]
        ni = ci-1
        
        # 앞에 있던 사람
        ai = ni
        player2 = dt[ai]
        players[ci] = player2
        players[ai] = player
        
        dt[ci] = player2
        dt[ai] = player
        dt[player] = ai
        dt[player2] = ci
        
    return players