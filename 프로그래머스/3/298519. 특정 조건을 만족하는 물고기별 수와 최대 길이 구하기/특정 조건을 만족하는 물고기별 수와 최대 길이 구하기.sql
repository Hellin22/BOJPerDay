SELECT COUNT(*) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
WHERE FISH_TYPE IN (
SELECT FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(CASE WHEN LENGTH IS NULL THEN 10 ELSE LENGTH END) >= 33
# ORDER BY AVG(GREATEST(LENGTH, 10)) DESC;
)
GROUP BY FISH_TYPE
ORDER BY FISH_TYPE ASC