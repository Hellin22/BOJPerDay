'''
numbers의 각 자리수를 모두 사용할 수 있는 변수로 적용한다.
같은 숫자가 있을 수 있다. -> 현재 값은 사용하지 못한다.
visit 배열을 사용해?
소수인지 확인할 필요가 있음 -> 최대값을 찾아서 그 최대값 만큼의 배열 선언(2차원)
최대는 9,999,999이겠지?  천만개의 배열
-> 메모리 초과는 안날거같음. -> 만약 메모리초과가 난다면? 
9876543가 최대임 -> 7!가지 -> 7!은?
7 6 5 4 3 2
42 20 6 -> 120 42 -> 4000(5000) 5백만 * 5000 -> 5,000,000,000 안되.ㅁ 절대 안됨ㅁ.

그러면 이제 어떤걸 사용할지를 정해야함.
-> dfs(몇개를 고를건지, 현재 idx)
    if 고른 개수가 == cnt라면 
visit = [0] * len(numbers) -> "17" 이라면 2만큼의 크기임. -> 1 / 7 / 1 7
dfs(1, 0)

그러면 그냥 itertools에서 

'''
import itertools
import math

def solution(numbers):
    answer = 0
    
    n = len(numbers)
    # visit = [0] * n
    
    # llist = itertools(range(0, n), 1) # 1도 하고 
    # 어떤 리스트를 파라미터로 줘야하는가? a라는 리스트를 준다고 해보자.
    a = []
    for i in range(n):
        a.append(i)
    st = set()
    for i in range(1, n+1):
        llist = list(itertools.permutations(a, i))
        for j in range(len(llist)):
            sttr = ""
            # [(0,), (1,), (2,)]
            # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
            for k in range(len(llist[j])):
                sttr+=str(numbers[llist[j][k]])
                st.add(int(sttr))
        
    maxx = max(st)
    is_sosu = [0] * 10000000
    is_sosu[0] = 1
    is_sosu[1] = 1
    for i in range(2, int(math.sqrt(maxx))+1):
        if is_sosu[i] == 1: continue
        for j in range(i+i, 10000000, i):
            if is_sosu[j] == 0:
                is_sosu[j] = 1
    for val in st:
        if is_sosu[val] == 0:
            answer+=1
    
    
    return answer