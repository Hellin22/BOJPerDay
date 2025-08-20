from itertools import permutations, product

def solution(numbers, target):
    '''
    최대 20개라 ㄱㅊ
    +인지, -인지만 선택하면 됨.
    
    0인지, 1인지를 선택하게하기
    +++++
    ++++-
    +++-+
    +++--
    ++-++
    ++--+
    '''
    a = 0
    ans = 0
    def dfs(i):
        nonlocal a, ans, target
        # print(i, a, ans)
        if i == len(numbers):
            if a == target: ans+=1
            return
        a+=numbers[i]*1
        dfs(i+1)
        a+=numbers[i]*-2
        dfs(i+1)
        a+=numbers[i]*1
    
    dfs(0)
    # print(a, ans)
    return ans