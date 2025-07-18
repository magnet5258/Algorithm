-- 코드를 작성해주세요
SELECT F.ID, FNI.FISH_NAME, FI.LENGTH
FROM (
    SELECT FISH_TYPE, MAX(LENGTH) AS LENGTH
    FROM FISH_INFO
    GROUP BY FISH_TYPE
) AS FI
INNER JOIN FISH_NAME_INFO AS FNI
ON FI.FISH_TYPE = FNI.FISH_TYPE
INNER JOIN FISH_INFO AS F
ON FI.FISH_TYPE = F.FISH_TYPE AND FI.LENGTH = F.LENGTH
ORDER BY F.ID;