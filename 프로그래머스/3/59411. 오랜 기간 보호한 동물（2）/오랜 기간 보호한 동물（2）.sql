/*
입양을 간 동물 중, 보호 기간이 가장 길었던 동물 2마리의 아이디와 이름 조회
-> 입양을 무조건 갔어야함.
-> 보호 기간이 가장 길었던 것 중 2마리 limit 2
즉, in에도 있고 out에도 있는것.
inner join 쓰기 -> ANIMAL_OUTS 기준으로 left outer join 해도 될듯
IN의 DATETIME하고 OUT의 DATETIME을 비교해서 가장 긴 친구 2마리
*/

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A
INNER JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(A.DATETIME, B.DATETIME) ASC
LIMIT 2