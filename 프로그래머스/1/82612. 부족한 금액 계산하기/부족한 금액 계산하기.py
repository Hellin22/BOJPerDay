def solution(price, money, count):
    return 0 if sum(list(i for i in range (1, count+1)))*price - money < 0 else sum(list(i for i in range (1, count+1)))*price - money