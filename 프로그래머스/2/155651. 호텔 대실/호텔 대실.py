'''
1. book_time 분으로 처리
2. book_time 시작시간 별로 정렬
3. llist에 추가해야함 (종료시간)
4. 어떤걸 추가할때에 llist를 돌면서 종료시간+10을 했는데 그게 현재 시작시간보다 작다 == 빼고 넣ㅇ르 수 있음
1000개니까 1000*1000 -> 가능할거로 예상
'''
def solution(book_time):
    answer = 0
    # 1. 분으로 처리
    for i, val in enumerate(book_time):
        a, b = val[0], val[1]
        abun = int(a[0]) * 600 + int(a[1]) * 60 + int(a[3]) * 10 + int(a[4])
        bbun = int(b[0]) * 600 + int(b[1]) * 60 + int(b[3]) * 10 + int(b[4])
        book_time[i] = [abun, bbun]
        
    # 2. 앞에껄로 정렬
    book_time.sort(key = lambda x: (x[0], x[1]))
    
    # 3. llist에 추가하기
    llist = [0]
    for idx, val in enumerate(book_time):
        flag = True
        for i in range(len(llist)):
            if llist[i] + 10 <= val[0]:
            # 종료시간이 들어있는데 이거 + 10을 했는데 현재 시작시간이 더 크다?
            # 빼고 현재꺼 넣을 수 있는것
                llist[i] = val[1]
                flag = False
                break
        if flag: # 새로운 리스트를 만들어서 추가해야함.
            llist.append(val[1])
    
    
    
    
    
    
    return len(llist)