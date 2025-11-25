import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    # 0 0 0 이면 종료
    if a == 0 and b == 0 and c == 0:
        break

    # 가장 긴 변을 구하고, 나머지 두 변의 합을 계산
    m = max(a, b, c)
    total = a + b + c

    # 삼각형이 될 수 없는 경우
    if m >= total - m:
        print("Invalid")
    # 세 변이 모두 같은 경우
    elif a == b == c:
        print("Equilateral")
    # 두 변만 같은 경우
    elif a == b or b == c or a == c:
        print("Isosceles")
    # 모두 다른 경우
    else:
        print("Scalene")
