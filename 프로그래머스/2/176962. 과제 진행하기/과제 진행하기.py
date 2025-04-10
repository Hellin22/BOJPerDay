'''
과제 진행
1. 현재 시간에 과제 해야함 -> 과제 진행

2. 다 끝냈다면 이전에 못한거 수행 -> 만약 새로운 과제 해야하면 그거 우선임

3. 다 못끝냈는데 새로운 과제 해야함 -> 못끝낸거 넣고 새로운 과제 수행

이전에 못한거 수행할때는 가장 최근에 못끝낸거를 진행함.
이거 딱 봐도 pq를 써야할듯
-> 가장 최근에 멈춘 과제부터 수행 -> pq에는 (과제 멈춘 시간, 남은 시간, "이름") 이렇게 넣어야할듯



'''
import heapq

def solution(plans):
    answer = []
    
    for i, val in enumerate(plans):
        ttime = int(val[1][:2]) * 60 + int(val[1][3:])
        plans[i] = [val[0], ttime, int(val[2])]
    
    plans.sort(key = lambda x: (x[1]))
    hq = []
    cur_time = plans[0][1]
    
    for i in range(len(plans)-1):
        # [['music', 740, 40], ['computer', 750, 100], ['science', 760, 50], ['history', 840, 30]]
        plan1 = plans[i]
        plan2 = plans[i+1]
        # cur_time을 계속 갱신할 필요가 있음
        cur_time = plan1[1]
        
        
        if plan1[1] + plan1[2] < plan2[1]:
            # 현재꺼를 끝낼 수 있다는 의미
            answer.append(plan1[0])
            cur_time = plan1[1] + plan1[2]
            while hq:
                # 현재 시간
                # -1*과제 멈춘시간, 남은시간, "이름"
                new_pl = heapq.heappop(hq)
                # 남은시간 + cur_time 했는데 plan2[1]보다 작거나 같다?
                # 그리고 같다면 즉, ==이면 hq 종료해야함.
                if new_pl[1] + cur_time <= plan2[1]:
                    answer.append(new_pl[2])
                    cur_time += new_pl[1] 
                    if cur_time == plan2[1]:
                        break
                        
                else: # 제일 중요한 부분, 중간에 진행하다가 다시 hq에 넣어야함.
                    # 얼마나 진행했는지를 알아야함.
                    # new_pl[1]만큼 해야하는데 cur_time ~ plan2[1] 보다 큰거임.
                    # cur_time = plan2[1] 
                    # plan2[1] - cur_time 만큼을 줄이기
                    heapq.heappush(hq, (-plan2[1], new_pl[1] - (plan2[1]-cur_time), new_pl[2]))
                    cur_time = plan2[1]
                    break
        
        elif plan1[1] + plan1[2] == plan2[1]: 
            answer.append(plan1[0])
            cur_time = plan2[1]

                
        elif plan1[1] + plan1[2] > plan2[1]:
            heapq.heappush(hq, (plan2[1] * -1, plan1[2] - (plan2[1] - plan1[1]), plan1[0]))
            cur_time = plan2[1]
            # 뭘 집어넣어야함? -> -1*과제 멈춘시간, 남은시간, "이름"
            # plan2[1] * -1, plan2[1] - plan1[1], "plan1[0]"
    
    answer.append(plans[-1][0])
    while hq:
        new_pl = heapq.heappop(hq)
        answer.append(new_pl[2])
    return answer