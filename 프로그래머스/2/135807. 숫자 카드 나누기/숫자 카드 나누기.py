'''
a의 모든 숫자를 나눌 수 있고 + b의 모든 숫자를 못나누는 최대 양의 정수
반대도 가능
배열 크기는 최대 50만개

A를 모두 나눌 수 있다 -> A의 최소공배수 -> 나눌 수 있는거니까 공약수로 가야할듯??
B를 하나도 나눌 수 없다. -> 최대 공약수가 아닌것?

결론
A, B의 최대공약수를 구함.
Agcd를 Barray에 대해서 나눠지는지 확인 -> 나눠지면 2번으로 / 끝까지 안나눠지면 answer = Agcd
Bgcd를 Aarray에 대해서 진행 -> 나눠지면 종료 / 끝까지 x -> answer = max(answer, Bgcd)
'''
import math
def solution(arrayA, arrayB):
    answer = 0
    
    gcdA, gcdB = arrayA[0], arrayB[0]
    for v in arrayA:
        gcdA = math.gcd(gcdA, v)
    for v in arrayB:
        gcdB = math.gcd(gcdB, v)
    
    flgA, flgB = True, True
    for v in arrayB:
        if v < gcdA: continue
        if v % gcdA == 0: 
            print(v, gcdA, v%gcdA)
            flgA = False
            break
    for v in arrayA:
        if v < gcdB: continue
        if v % gcdB == 0:
            flgB = False
            break
    print(gcdA, gcdB)
    if flgA:
        answer = gcdA
    if flgB:
        answer = max(answer, gcdB)
    return answer
