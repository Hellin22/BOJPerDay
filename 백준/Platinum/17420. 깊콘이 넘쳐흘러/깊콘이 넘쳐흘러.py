import sys
inp = sys.stdin.readline

# n개 기프티콘
# i번째 기프티콘 남은 기한 ai
# i번째 기프티콘 bi뒤에 사용 할 예쩡

# 1. (ai, bi)를 모두 넣은 배여 ㄹ유지
# 2. ai가 작은거 순서대로(먼저 사용해야하는 것) 정렬
# 3. 순서가 없으니까
# 4. 30-4 = 26 -> 1번
# 5. 10-10 - 0 -> 0번
# 6. 100-5 = 95 -> 4번
# 이렇게 하면 되나?
# 0이 아니라면 bi-ai // 30 +1


# 기한이 가장 적게 남은 기프티콘만 사용 가능 -> 여러개 한번에 사용 가능
# 이해가 안되는게 언제 쓸지 계획을 정해놓음. -> 기프티콘중 기한이 가장 적게 남은 기프티콘만 사용 가능.

# 기간이 가장 적게 남은 기프티콘만 사용 가능하다. 즉, 기간이 적게 해야한다.
# bi 기준으로 하는건 확실함.
# (10, 10), (100, 5), (30, 4)
# (10, 10), (30, 4), (100, 5)
# 현재 = 10 -> 현재 = 30 -> -26이니까 


n = int(inp().strip())
ai = list(map(int, inp().strip().split()))
bi = list(map(int, inp().strip().split()))
aibi = list(zip(ai, bi))

aibi.sort(key = lambda x: (x[1], x[0]))

max_a = 0
ans = 0
i = 0
while i < n:
    b = aibi[i][1] # 사용 날짜 -> 사용 날짜 동일한거 끼리 묶기
    group = []

    while i < n and aibi[i][1] == b:
        group.append(aibi[i][0])
        i+=1
    
    group.sort()
    group_max = -1
    for j in range(len(group)):
        a = group[j]
        # 여기서 나온 a 값 중 min 값으로 max_a를 초기화

        if a < b:
            need = b-a
            extend = (need + 29) // 30 # 얼마나 늘려야 하는지 (ex 3번)
            a += extend * 30 # a에 늘린 날짜 추가
            ans += extend # ans에 늘린 횟수 추가

        if a < max_a: # 조건 처리 -> 이전 값이 가장 짧은 유효기간 이었어야함.
            # 이전이 더 큰경우
            # max_a가 현재 a보다 큰경우 -> 조건 위배 -> a를 max_a보다 크게 만들어야함.
            # ex) max_a = 50 / a = 40 -> a = 70
            need = max_a - a
            extend = (need + 29) // 30 # 얼마나 늘려야하는지
            a += extend*30
            ans += extend

        # print(max_a, a)
        # max_a = max(max_a, a) # 최대값 갱신
        # group에서의 최대값이 나중에 max_a가 됨. 하지만 group 내에서는 max_a를 갱신하면 안됨.
        group_max = max(group_max, a)

    max_a = group_max


print(ans)



'''
4
24 2 3 29
25 30 30 30

'''