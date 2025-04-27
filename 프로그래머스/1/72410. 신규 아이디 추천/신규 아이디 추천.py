'''
알파벳 소문자, 숫자, -, _, . 사용가능
.은 처음과 끝에 못사용 + 연속 못사용

1. 대문자가 소문자로
2. 못쓰는 문자 삭제
3. ...과 ..은 .으로됨
4. 처음에 있는 .은 삭제
5. 빈문자열 이라면 a로 바꿈
6. 길이가 16자 이상이면 처음 15개 제외하고 없앰
 만약 마침표로 끝 -> 마침표 제거
7. 2자 이하라면 neww_id의 마지막 문자를 new_id 뒤에 계속 붙임(3이 될때 까지)

'''
def solution(new_id):
    answer = ''
    # 사용 가능한 문자는 str_set에 추가해놓기
    str_set = set()
    for i in range(97, 123):
        str_set.add(chr(i))
    for i in range(0, 10):
        str_set.add(str(i))
    str_set.add('.')
    str_set.add('_')
    str_set.add('-')
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()
    tmp_new_id = ""
    # 2. 못쓰는 문자 삭제
    for i in new_id:
        if i in str_set:
            tmp_new_id+=i
    new_id = tmp_new_id
    
    # 3. ...은 .으로 바꾸기
    jum_flag = False
    tmp_new_id = ""
    for i in range(len(new_id)):
        if new_id[i] != '.':
            jum_flag = False
            tmp_new_id+=new_id[i]
        else:
            if jum_flag: continue
            else: 
                tmp_new_id+=new_id[i]
                jum_flag = True
    new_id = tmp_new_id
    
    # 4. 처음과 끝 . 삭제
    if new_id:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    # 5. 빈문자열이면 a
    if not new_id:
        new_id = "a"
    
    # 6. 길이가 16자 이상이면 15개 제외하고 없앰
    new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    
    # 7. 2자 이하라면 3이 될때까지 끝에꺼 복사해서 붙임
    if len(new_id) == 1:
        new_id += new_id[-1]*2
    elif len(new_id) == 2:
        new_id += new_id[-1]
    
    answer = new_id
# 1. 대문자가 소문자로
# 2. 못쓰는 문자 삭제
# 3. ...과 ..은 .으로됨
# 4. 처음과 끝에 있는 .은 삭제
# 5. 빈문자열 이라면 a로 바꿈
# 6. 길이가 16자 이상이면 처음 15개 제외하고 없앰
#  만약 마침표로 끝 -> 마침표 제거
# 7. 2자 이하라면 neww_id의 마지막 문자를 new_id 뒤에 계속 붙임(3이 될때 까지)
    return answer