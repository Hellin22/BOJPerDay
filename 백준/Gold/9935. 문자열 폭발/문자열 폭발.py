import sys
inp = sys.stdin.readline


'''
문자열에 폭발 문자열이 있음.
폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지고 남은 문자열은 합쳐짐
모든 폭발 문자열이 폭발한다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을수도 있음.

모든 문자열이 폭발하고 어떤 문자열이 남는지 확인
""인 경우에 FRULA 출력

반복해서 split, join?
'''
sttr = inp().strip()
bomb = inp().strip()

stck = []
tmp_sttr = ""
for ch in sttr:
    # 어떤 순서로?
    # stck에 집어넣고 tmp_sttr에 붙여야함. 근데 tmp_sttr의 크기가 bomb보다 크면 앞에꺼 줄이기
    stck.append(ch)
    tmp_sttr += ch
    if len(tmp_sttr) > len(bomb):
        tmp_sttr = tmp_sttr[1:]

    while stck and tmp_sttr == bomb: # 폭탄문자열이면 stck에서 bomb만큼 빼기
        for i in range(len(bomb)):
            stck.pop()
        tmp_sttr = ""
        for i in range(len(stck)-1, -1, -1):
            tmp_sttr += stck[i]
            if len(tmp_sttr) == len(bomb): break # 길이 같아지면 종료
        tmp_sttr = tmp_sttr[::-1]

print(''.join(stck) if stck else "FRULA")