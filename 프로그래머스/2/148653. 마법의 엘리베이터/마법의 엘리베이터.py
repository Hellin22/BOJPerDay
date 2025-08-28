def solution(storey):
    '''
    0층이 제일 밑
    10^c만큼 이동 가능
    1억
    
    0층으로 가야함.
    2446 4번 + 1번 or 6번 -> 무조건 빼야함
    2556 
    5인 경우에만 좀 달라질거같음.
    5인 경우
    5번 빼든가 5번 더하든가
    5번 빼면 5번 / 5번 더하면 앞자리로 올라감.
    앞자리가 없으면 빼는게 맞음.
    앞자리가 있다면 5~9는 당연히 높이는게 맞음
    0~4는 빼는게 맞음
    '''
    ans = 0
    storey = str(storey)
    while storey != "":
        # 계속해서 제일 오른쪽꺼만 빼기
        print(storey, ans)
        
        
        # 1. 현재 값이 5 초과
        if int(storey[-1]) > 5: 
            ans += 10 - int(storey[-1])
            if storey[:-1] == "":
                storey = "1"
            else: 
                storey = str(int(storey[:-1])+1)
        # 2. 현재 값이 5 미만
        elif int (storey[-1]) < 5:
            ans += int(storey[-1])
            storey = storey[:-1]
        # 3. 현재 값이 5
        else:
            # 1. 5만 덩그러니
            if len(storey) == 1: 
                ans += 5
                storey = ""
            # 2. 5가 마지막이 아닌 경우
            else:
                # 1. 앞에 숫자가 0~4
                if 0 <= int(storey[-2]) <= 4:
                    ans += 5
                    storey = storey[:-1]
                # 2. 앞에 숫자가 5~9
                else:
                    ans += int(storey[-1])
                    storey = str(int(storey[:-1])+1)
                
    return ans
        