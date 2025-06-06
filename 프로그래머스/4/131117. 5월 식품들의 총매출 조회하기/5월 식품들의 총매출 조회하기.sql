/*
1. food_order에서 2022 4월꺼만 가져오기
2. food_order의 product_id하고 food_product의 product_id로 조인
3. 이게 2번이 됨. group by로 product_id로 group by로 묶기
4. amount하고 price랑 * 결과로 order by
*/

SELECT A.PRODUCT_ID, A.PRODUCT_NAME, (A.PRICE * B.AMT_SUM) AS TOTAL_SALES
FROM FOOD_PRODUCT AS A
JOIN (SELECT PRODUCT_ID, SUM(AMOUNT) AS AMT_SUM
        FROM FOOD_ORDER
        WHERE YEAR(PRODUCE_DATE) = 2022 AND MONTH(PRODUCE_DATE) = 5
        GROUP BY (PRODUCT_ID)) AS B
    ON A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC




