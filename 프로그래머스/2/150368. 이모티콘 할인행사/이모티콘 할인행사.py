'''
감이 안잡힘...
뭐 어떻게 푸는거지?
사람마다 할인율은 정해져있음.
근데 이모티콘은 할인율을 맘대로 바꿀 수 있음. -> 이모티콘 개수는 m개임
m은 최대 7개임. 즉, 100^7이 가능하다는 의미.
만약 최대 할인율을 토대로 한다해도 최대 할인율은 40임
즉, 40^7 == 2^14 * 10^7 이게 시간복잡도를 무조건 넘는다. 완탐은
이거 어캐풀지?
# ㅋㅋㅋ 할인율이 4개중에 하나구나...
4^7개의 조합이 나오는듯? -> 전체 다 풀어야함. * 100 2^14 = 1024 * 8 * 100 == 충분할듯
'''
import itertools
def solution(users, emoticons):
    cnt, moneySum = -1, -1
    # cnt가 우선임
    
    halin = [10, 20, 30, 40] # 가격 * halin[llist[i]] // 100 하기
    llist = [] # 어떤거를 의미하는지
    
    def check():
        nonlocal cnt, moneySum
        # 이모티콘의 할인율을 적용해서 가격 계산해놓기
        realPrice = []
        allPay = 0
        plusCnt = 0
        for i in range(len(emoticons)):
            realPrice.append(emoticons[i] * (100-halin[llist[i]]) // 100)
        # realPrice는 이모티콘에 할인 먹힌 가격이 있음.
        # 사람수만큼 돌면서 1. 할인율 보고 2. 사람 할인율이 halin[llist[i]]보다 작거나 같으면 구매(20, 40)이면 구매하는것 3. 만약 가격 합이 10000이 넘어가면 plusCnt+=1  break 4. 안넘어가면 allPay+=1
        for halinyul, money in users:
            # 사람이 원하는 할인율, 한계 금액
            curPay = 0
            for i, val in enumerate(llist): # llist
                if halinyul <= halin[val]: # 금액 더해주기
                    curPay+=realPrice[i]
                if curPay >= money:
                    plusCnt+=1
                    break
            if curPay < money:
                allPay += curPay
        # print("전역", cnt, moneySum, "지역", plusCnt, allPay)
        # print("할인 얼만지", llist)
        # print("할인 이모티콘 가격", realPrice)
        # 만약 plusCnt가 cnt보다 크다? 바로 교체
        # 둘이 동일하다 -> moneySum = max(moneySum, allPay)
        if plusCnt > cnt: cnt, moneySum = plusCnt, allPay
        elif plusCnt == cnt: moneySum = max(moneySum, allPay) 
        
    def permut(): # 어떤게 필요하지?  중복 순열인거같네
        # 파라미터가 아예 피룡 없을거같음.
        if len(llist) == len(emoticons):
            # 실제 금액, 플러스 가입 수 계산하는 함수 필요!!!!!!!
            check()
            return
        
        for i in range(4):
            llist.append(i)
            permut()
            llist.pop()
    
    
    
    permut()
    
       
    return [cnt, moneySum]
