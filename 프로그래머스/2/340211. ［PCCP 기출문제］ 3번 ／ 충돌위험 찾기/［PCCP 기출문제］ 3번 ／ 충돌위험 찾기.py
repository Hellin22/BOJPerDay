directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def solution(points, routes):
    answer = 0
    points = [[0, 0]] + points
    routes = [[0, 0]] + routes
    cur_coor = [[0, 0] for _ in range(len(routes))]
    cur_routes = [0] * (len(routes))
    st = set() # st는 현재 이동 가능한 로봇 번호를 추가하기 (1, 2, 3, 4)
    dictt = {} # dictt에는 좌표를 추가하기 ((1, 2):1, (2, 4):2)
    
    # 1. cur_coor 초기화 해주기
    for i in range(1, len(routes)): # routes의 개수 = 로봇의 개수 0~n
        cur_coor[i] = [points[routes[i][cur_routes[i]]][0], points[routes[i][cur_routes[i]]][1]]
        dictt[(cur_coor[i][0], cur_coor[i][1])] = dictt.get((cur_coor[i][0], cur_coor[i][1]), 0) + 1
        st.add(i) # st에는 로봇 번호가 있음.
        
    for val in dictt.values():
        if val > 1:
            answer+=1
        
    # 2. cur_coor을 이동하면서 겹치는게 있는지 확인해야함. -> dict에 저장
    remain = len(routes) # 로봇의 개수
    cnt = 0
    # while cnt != 20:
    while len(st) != 0: # 로봇이 0개가 아니라면 이동해야함.
    
        # print("현재 좌표", cur_coor[1:])
        # print("현재 루트", cur_routes[1:])
        # print(answer)
        dictt.clear()
        
        # 로봇들을 한칸씩 이동해야함. -> 어떤 로봇? st 안에 있는 로봇들
        stt = list(st)
        st.clear()
        for i in stt:
            # i는 로봇 번호
            # i번 로봇의 현재 좌표는 cur_coor[i][0], cur_coor[i][1]
            # i번 로봇의 현재 루트는 cur_routes[i]
            # i번 로봇이 현재 가야하는 좌표는 points[routes[i][cur_routes[i]+1]]
            # 만약 i번 로봇이 points[routes[i][cur_routes[i]+1]] 로 가는데 동일하다면 cur_routes[i]+=1
            # 만약 cur_routes[i]가 len(routes[i])와 동일하다면 st에는 추가x, dictt에는 추가o
            rbtx, rbty = cur_coor[i][0], cur_coor[i][1]
            wantx, wanty = points[routes[i][cur_routes[i]+1]]
            
            for dx, dy in directions:
                nx = rbtx + dx
                ny = rbty + dy # 옮긴 후에 더 가까워져 있어야함.
                if 0 < nx and 0 < ny and abs(nx - wantx) + abs(ny - wanty) < abs(rbtx - wantx) + abs(rbty - wanty):
                    # 더 가까워졌다면 -> 그걸로 진행.
                    # 좌표 갱신, dictt에 추가, st에 추가, 만약 새로운 포인트라면 포인트 교체
                    # 새로운 포인트가 종료지점이라면 st에는 추가x
                    if (nx, ny) == tuple(points[routes[i][cur_routes[i]+1]]):
                        # 같다면 
                        cur_routes[i]+=1
                        cur_coor[i] = [nx, ny]
                        dictt[(cur_coor[i][0], cur_coor[i][1])] = dictt.get((cur_coor[i][0], cur_coor[i][1]), 0) + 1    
                        if cur_routes[i] != len(routes[i])-1:
                            st.add(i)
                            break
                    else:
                        cur_coor[i] = [nx, ny]
                        dictt[(cur_coor[i][0], cur_coor[i][1])] = dictt.get((cur_coor[i][0], cur_coor[i][1]), 0) + 1
                        st.add(i)
                        break
            
        # 마지막에는 dictt를 돌면서 val이 2 이상이면 answer++
        for val in dictt.values():
            if val > 1: answer+=1
            
        cnt+=1
            
    return answer





