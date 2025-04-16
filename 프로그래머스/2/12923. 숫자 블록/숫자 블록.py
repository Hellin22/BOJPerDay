'''
어떤 수 * 2부터 ~ 끝까지 전부 해당 숫자로 칠해짐

만약에 어떤수에 머가 칠해져있느냐?
1793에는 어떤 수임?

1793/2 -> 1793/3

만약에 소수라면? -> 1이 적힘
소수가 아니라면? -> gcd로 나눈 수가 적힐거같음.
근데 소수인지 아닌지를 10억개가 되는데 만약 10개의 배열을 준다고하면
아 5000개임.
그러면 소수판별은 알아서 하는걸로하고 나머지는 math.gcd로 처리하고나서 이 gcd를 

cur//gcd->적혀있는 값이지 않을까 싶은데

why? 소수는 해당 값 *2부터 그 값이 적힘.
소수가 아니라면 gcd(가장 가까운 값)로 나눈 값이 적히게됨
gcd를 이런식으로 처리하는게 맞나? -> gcd는 최대공약수 -> 2개의 값에 대한 공통 공약수 의미
그냥 공약수 중에 가장 큰거를 리턴해야함.

'''
# 천만까지있음.
def solution(begin, end):
    answer = []
    
    def is_prime(num):
        minn = int(num**0.5) +1
        maxx = -1
        for i in range(2, minn):
            if num % i == 0:
                # 지금 num//i가 답인데 i를 설정해서 그럼.
                
                if i <= 10000000:
                    maxx = max(maxx, i)
                    if num//i <= 10000000:
                        
                        maxx = max(maxx, num//i)

        if maxx != -1: return False, maxx
        return True, 1
    # [0,1,1,2,1,3,1,4,3,5,
    # 1,6,1,7,5,8,1,9,1,10]
    for i in range(begin, end+1):
        # i가 소수인지 알아야함.
        if i == 1: 
            answer.append(0)
            continue
        flag, num = is_prime(i)
        if not flag: answer.append(num)
        else: answer.append(num)
    
    return answer