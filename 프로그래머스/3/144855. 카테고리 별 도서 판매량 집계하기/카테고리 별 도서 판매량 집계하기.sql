/*
1. 2022년 1월 도서별 총 판매량 (SALES_DATE의 YEAR, MONTH 고려)
2. SALES의 개수가 존재함 -> BOOK_ID GROUP BY하고 SALES의 SUM으로 RS 만들기
3. BOOK TBL과 조인해서 CATEGORY 이름 가져오기(BOOK_ID 빼고)
4. 카테고리순으로 정렬(오름차)
*/

SELECT A.CATEGORY, SUM(B.TOTAL_SALES)
FROM BOOK AS A
JOIN (
SELECT BOOK_ID, SUM(SALES) AS TOTAL_SALES
FROM BOOK_SALES
WHERE YEAR(SALES_DATE) = '2022' AND MONTH(SALES_DATE) = '01'
GROUP BY BOOK_ID
) AS B
ON A.BOOK_ID = B.BOOK_ID
GROUP BY CATEGORY
ORDER BY A.CATEGORY ASC
