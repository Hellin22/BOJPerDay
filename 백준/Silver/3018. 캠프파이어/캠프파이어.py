import sys 
inp = sys.stdin.readline

partyPeopleCnt = int(inp().strip())
partyCnt = int(inp().strip())

# set을 가지고 있는 list를 만들어야함.
list_set = [set() for _ in range(partyPeopleCnt + 1)]
song_cnt = 0
for i in range(partyCnt):
    llist = list(map(int, inp().strip().split()))
    cnt = llist[0]
    sunyoungFlag = False
    
    # 이제 사람들에 대해서 저걸 진행해야함. -> 일단 선영이의 유무부터 파악
    for j in range(1, len(llist)):
        if llist[j] == 1:
            sunyoungFlag = True
            break

    if sunyoungFlag == True: # 선영이가 존재 -> 나머지 사람들이 1개 새로운노래 부름름
        for j in range(1, len(llist)):
            if llist[j] == 1: continue
            else:
                list_set[llist[j]].add(song_cnt)
        
        song_cnt+=1
    
    else: # 선영이가 없어서 모든 노래 공유해야함. -> 시간복잡도 가능한가?
        all_set = set()
        for j in range(1, len(llist)):
            all_set = all_set.union(list_set[llist[j]])
        
        for j in range(1, len(llist)):
            list_set[llist[j]].update(all_set)

print(1)
for i in range(2, partyPeopleCnt+1):
    if(len(list_set[i]) == song_cnt):
        print(i) 