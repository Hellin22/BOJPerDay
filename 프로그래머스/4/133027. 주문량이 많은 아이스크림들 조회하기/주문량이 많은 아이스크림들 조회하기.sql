-- 코드를 입력하세요
# 7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개
# TOTAL_ORDER의 합 큰거 3개?
# GROUP BY로 이름 묶기 -> TOTAL_ORDER의 합을 구해야함.

SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS JULY_ORDER
        FROM JULY
        GROUP BY(FLAVOR)) AS B 
    ON A.FLAVOR = B.FLAVOR
ORDER BY (A.TOTAL_ORDER + B.JULY_ORDER) DESC
LIMIT 3

