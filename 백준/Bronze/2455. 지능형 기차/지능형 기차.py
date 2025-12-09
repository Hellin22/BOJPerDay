current = 0      # 현재 기차 안 사람 수  
max_people = 0   # 최대 탑승 인원  

for _ in range(4):
    out_cnt, in_cnt = map(int, input().split())
    current -= out_cnt
    current += in_cnt
    if current > max_people:
        max_people = current

print(max_people)
