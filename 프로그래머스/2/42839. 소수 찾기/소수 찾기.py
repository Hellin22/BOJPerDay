def solution(numbers):
    '''
    numbers를 각 1개씩 나누기
    
    1~7의 길이 최대 9999999 천만개
    '''
    is_prime = [1] * 10000000
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, 10000000):
        if is_prime[i] == 1:
            for j in range(i*i, 10000000, i):
                is_prime[j] = 0
    
    num_list = list(numbers)
    num = ""
    st = set()
    visit = [0] * len(num_list)
    
    def dfs(idx):
        nonlocal num
        if len(num) == len(numbers):
            if is_prime[int(num)] == 1: st.add(int(num))
            return
        else:
            if num != "" and is_prime[int(num)] == 1: 
                st.add(int(num))
            for i in range(len(num_list)):
                if visit[i] == 0:
                    num+=num_list[i]
                    visit[i] = 1
                    dfs(i)
                    visit[i] = 0
                    num = num[:-1]
                    
    for i in range(len(num_list)):
        visit[i] = 1
        num = num_list[i]
        dfs(i)
        visit[i] = 0
    return len(st)