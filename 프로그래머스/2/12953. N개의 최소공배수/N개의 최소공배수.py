'''
여러개 수 중에서 최소 공배수 구하기
계속 반복하면서 최소공배수 구하기?
최소공배수는?
a * b / gcd = lcm

gcd는? a > b
a / b = c - d
b / c = k - e

8/6 = 1 - 2
6 / 2 = 3 - 0

14 / 8 = 1 - 6
8 / 6 = 1 - 2
6 / 2 = 3 - 0

e가 0이 될때까지?
'''
def solution(arr):
    
    def gcd(a, b):
        # 항상 a가 b보다 큼
        c, d = 111111, 111111
        while d != 0: # 나머지가 0이 아니면 반복
            c, d = a // b, a%b
            if d == 0: return b
            
            a, b = b, d
    
    
    arr.sort(key = lambda x: -x)
    gcd_num = arr[0]
    ans = arr[0]
    for i in arr[1:]:
        gcd_num = gcd(ans, i)
        ans *= i
        ans//=gcd_num
    
    return ans