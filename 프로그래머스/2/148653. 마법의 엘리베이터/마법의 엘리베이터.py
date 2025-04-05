'''
항상 최소한의 버튼 -> storey에서 0으로 가려고함.
bfs?
일단 내려가야하니까 +는 나중에 넣기
최대 제한은 1억임.
즉, -1억 ~ 1억까지 다 더해서 해주는데
0을 넘거나 1억을 넘으면 안함. -> 1억은 애초에 불가능
천만단위로 시작

결국 8 제곱수만큼 증가함. 모든게 다 증가하지는 않겠지만
너무 많이 적용되게됨.
즉, 저기서 안눌러도 되는 버튼이 존재한다는 의미
그걸 어떻게 필터링 할지를 선택해야함.
11 이라면 -1 보다는 -10
-11이라면 1 보다는 -10

즉, 천만 ~ 1까지 //를 확인하면 0이 안나오는 최초 지점 -> -11이면 10임
-11 // 10을 하면 -2가 나옴. -> -2와 9임.

1. 만약 cur_stair이 음수 -> 생각해보니까 음수는 불가능하구나.. ㅋㅋㅋ

1. cur_stair에 대해서 // 진행 -> 0이 안나오면 그걸로 진행하기
answer+= 몫
cur_stair = cur_stair - 몫 * 100 같은거
answer += 몫

'''
    
def solution(storey):
    answer = 0
    
    while storey != 0:
        print(storey)
        a = storey % 10
        if 1 <= a <= 4:
            answer += a
        elif 6<= a <= 9:
            answer+= 10-a
            storey+=10-a
        if a == 5:
            b = storey % 100 // 10
            # b = int(str(storey % 100)[0])
            
            # 앞에꺼가 존재하는지부터 확인
            if storey == 5:
                answer+=5
                break
            
            print(str(storey % 100)[0], storey, a, b)
            
            if 0 <= b <= 4: # 앞에꺼가 0~4라면 빼기
                answer+=a
            else:
                answer += 10-a
                storey+=10-a
                
        storey//=10
    return answer
    
    
#     for i in range(1, 9):
#         cur = storey
#         ten_jegob = 10**i
#         print(cur%ten_jegob, cur, ten_jegob)
#         a = int(str(cur%ten_jegob)[0])
#         print(a)
        
#         if a == 0: continue
#         elif 1 <= a <= 4:
#             answer+=a
#             cur -= a * ten_jegob//10
#         elif 6 <= a <= 9:
#             answer += 10-a
#             cur += (10-a) * ten_jegob//10
            
#         elif a == 5: # a가 5이면 그 앞에꺼를 봐야함.
#             # 앞에꺼가 0~4라면 빼기, 앞에꺼가 5~9라면 올리기
#             # 앞에꺼를 보는 방법은 ten_jegob*10을 해서 함 더구하면 됨.
#             b = int(str(cur%(ten_jegob*10))[0])
            
#             if 0 <= b <= 4: # 앞에꺼가 0~4라면 빼기
#                 answer+=a
#                 cur -= a * ten_jegob//10
#             else:
#                 answer += 10-a
#                 cur += (10-a) * ten_jegob//10
                
            
        
#         print("??", cur)
#         storey = cur
#         if storey == 0: return answer
    
    
    
    
    
    
    
    
    
    
#     def is_mod(num): # 어떠한 수 -> 이거 몫이 뭐냐에 따라서 +하거나 -해야할듯
#         # 반대로 해야하는구나....
#         # 즉, 작은 숫자부터 없애는 방식으로 진행.
#         # 그런데 그러면 현재값의 앞에있는거도 봐야하잖아.
#         # 44임 -> 4번4번
#         # 44임 -> 6 5 11번
#         # 54임 -> 5 4 9번
#         '''
#         54 -> 6 번 60 -> 4 1 -> 11번
#         64 -> 4번 5번
#         65 -> 5번(5인 경우는 앞에꺼를 보고해야함.) 5가 아니면 그냥 하면 될듯?
#         5인 경우 == 그 앞에께 있다면 -> 1. 그 앞에꺼도 5면 어캄?
#         455 5 5 4 -> 5 4 5
#         655 5 5 6 -> 5 5 4 -> 5 4 3 1
#         내생각에 5인 경우에 앞에껄 보는데 앞에께 5 이상이면 올림하는게 나은거같음
        
#         355 5 4 4 -> 5 5 3 -> 
        
#         한번의 함수로 진행하자.
#         1. 만약 cur을 %10이 56(6) 0이 아니라면
#             그 값에 대해서 진행.
#             만약 cur%100이 있다면 
            
#             -> 그냥 str로 진행?
#             sttr의 앞에서부터 보면되잖아.
#             int(sttr[i])가 5라면 / 0~4라면 / 6~9라면 -> 올림이 들어가는경우 문제가 생기네
#             그냥 int로 진행하자.
            
            
        
#         '''
        
#         nonlocal answer
#         # 예를 들어서 16은 1이니까 -10을 해줬는데 56은? -50이 나음. 66은? 106이 나음.(40)
#         # 그러면 몫에 따라서 몫이 1~5이면 -해주기, 몫이 6~9이면 +해주기
#         # 천만 = 10000000 -> 10**7 10,000,000
#         for i in range(7, -1, -1):
#             cur = 1*(10**i) # 천만 ~~ 1
#             if num // cur != 0: # 만약 현재값을 나눈 몫이 0이 아니면 그걸로 나누면 됨.
#                 if num//cur <= 5: # 5이하면 빼줘야함. 56이라면 50을 빼줘야함.
#                     answer+=num//cur
#                     return num%cur   # num이 어캐 바뀌는지를 해주면 될듯?
#                 else: # 9이면 1개 8이면 2개 (10에서 뺌)
#                     if cur == 10**7: # cur이 천만이라면? 위에꺼처럼 진행하기
#                         answer+=num//cur
#                         return num%cur
                                
                    
#                     answer+= 10 - num//cur # 66이람면 40을 더해야함.즉, 106이 되면됨.
#                     # num%cur = 6 -> cur*10
#                     return cur*10 + num % cur 
#                 # 문제ㅔ는 6천 오백만 -> 1억 오백만이됨. -> 1억이 안넘게 하기
#                 # 즉, 천만이 넘는데 저거면 그냥 빼줘야함.
    
#     while(True):
#         storey = is_mod(storey)
#         if storey == 0:
#             return answer
        
        
        
        
        
        