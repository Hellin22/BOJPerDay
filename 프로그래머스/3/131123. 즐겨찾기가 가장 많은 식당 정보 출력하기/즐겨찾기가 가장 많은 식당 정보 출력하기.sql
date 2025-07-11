/*
0. 서브쿼리 지양하기
1. REST_INFO에서 음식종류별로 즐겨찾기수가 가장 많은 식당만 남기기

*/
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN(
SELECT FOOD_TYPE, MAX(FAVORITES)
FROM REST_INFO
GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC
