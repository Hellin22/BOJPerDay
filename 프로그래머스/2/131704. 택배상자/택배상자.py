
def solution(order):
    
    '''
    4 3 1 2 5
    5
    321
    43
    
    stck과 llist
    '''
    stck = []
    llist = [len(order)-i for i in range(len(order))]
    ans = 0
    order = order[::-1]
    while order:
        if stck and order[-1] == stck[-1]: # stck의 top이 해당 값이라면
            order.pop()
            stck.pop()
            ans+=1
        else:
            flag = False
            while llist:
                if order[-1] != llist[-1]:
                    stck.append(llist.pop())
                else: 
                    flag = True
                    llist.pop()
                    order.pop()
                    ans+=1
                    break
            if not flag: break

    return ans