# ANIMAL_INS
# ANIMAL_OUTS

# 입양 간 기록(OUTS)에는 있는데 보호소에 들어온 기록(INS)는 없는거
# 동물 ID, 이름 -> 동물ID 순으로 조회

# right outer join? -> 한곳에만 있어야하니까 ㅇㅇ
# 이름이 없는거만....
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I
    RIGHT JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID

# NULL이면 되나?