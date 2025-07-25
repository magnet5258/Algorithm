-- 코드를 작성해주세요
SELECT COUNT(ID) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM (
    SELECT
        ID,
        FISH_TYPE,
        CASE
            WHEN LENGTH IS NULL THEN 10
            WHEN LENGTH <= 10 THEN 10
            ELSE LENGTH
        END AS LENGTH
    FROM FISH_INFO
) AS SUB
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE;

