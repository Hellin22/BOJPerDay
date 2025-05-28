'''
lcm 찾는 문제
lcm은 모든 곱 / gcd
gcd -> 유클리드 호제법
gcd(a, b) = gcd(b, r(a%b)) -> r이 0이 될때까지

n개를 gcd하면?
모든거를 gcd해서 나온거중 최소값?


'''
def solution(arr):
    
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    
    return result

def gcd_def(a, b):
    if b == 0:
        return a
    if b != 0:
        return gcd_def(b, a%b)

def lcm(a, b):
    return (a*b) // gcd_def(a, b)

