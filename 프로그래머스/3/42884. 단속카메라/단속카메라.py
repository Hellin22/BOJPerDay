'''
진입한 지점, 나간 지점이 주어짐
이거 많이 풀어봤던거네

끝에꺼 기준으로 정렬을 하는문제?
[[-20,-15], [-18,-13], [-14,-5], [-5,-3]] 2

[1 2] [3 4] [4 5]

# 어떤걸 기준으로 새로운거의 끝이 처음의 기준의 처음보다 작다면
# 계속 진행
# 만약 기준의 처음보다 작다. 즉, [3 5] [6 8] 이거는 5가 더 작음 -> 새로운거 해야함.

'''

def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x: (x[1], x[0]))
    # 1 2  3 4   5 6
    i = 0
    while i <= len(routes):
        answer+=1
        flag = True
        for j in range(i+1, len(routes)):
            print(i, j)
            if routes[j][0] > routes[i][1]:
                i = j
                print(i)
                flag = False
                break
        if flag: break
    
    
    return answer