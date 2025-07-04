# /*
# USED_GOODS_BOARD
# USED_GOODS_USER

# 게시글 3개이상 등록한 사용자

# 주소는 시, 도로명주소, 상세주소 같이 출력되게 -> 합치는거 필요
# 전화번호는 하이폰(-)로 구분해야함.
# */

# SELECT A.WRITER_ID AS USER_ID, B.NICKNAME, CONCAT(B.CITY, B.STREET_ADDRESS1, B.STREET_ADDRESS2) AS '전체주소', CONCAT(SUBSTR(B.TLNO, 1, 3), '-', SUBSTR(B.TLNO, 4, 4), '-', SUBSTR(B.TLNO, 8, 4)) AS '전화번호'
# FROM USED_GOODS_BOARD AS A
# INNER JOIN USED_GOODS_USER AS B
# ON A.WRITER_ID = B.USER_ID
# GROUP BY 
#   A.WRITER_ID,
#   B.NICKNAME,
#   B.CITY,
#   B.STREET_ADDRESS1,
#   B.STREET_ADDRESS2,
#   B.TLNO
# HAVING COUNT(A.WRITER_ID) >= 3
# ORDER BY USER_ID DESC

SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소', CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 8, 4)) AS '전화번호'
FROM USED_GOODS_USER
WHERE USER_ID IN (
SELECT WRITER_ID AS USER_ID
FROM USED_GOODS_BOARD
GROUP BY WRITER_ID
HAVING COUNT(*) >= 3
)
ORDER BY USER_ID DESC
