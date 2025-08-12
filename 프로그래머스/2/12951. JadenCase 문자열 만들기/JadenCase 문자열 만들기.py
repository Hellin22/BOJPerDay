'''
첫문자 대문자
그외는 소문자인 문자열
첫문자 알파벳 아니면 소문자로 쭉 쓰면됨.

저걸로 바꿔서 리턴하게 바꾸기

-> 소문자 -> 대문자로 바꾸는법
upper_case

연속된 공백 가능
'''

def solution(s):
    answer = ''
    flg = True
    
    for i in s:
        answer += i.upper() if flg else i.lower()
        flg = (i == ' ')
        
    return answer
    