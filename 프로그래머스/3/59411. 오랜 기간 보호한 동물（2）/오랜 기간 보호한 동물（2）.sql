-- 코드를 입력하세요
SELECT AO.ANIMAL_ID, AO.NAME
FROM ANIMAL_INS AS AI
INNER JOIN ANIMAL_OUTS AS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
ORDER BY (AO.DATETIME - AI.DATETIME) DESC
LIMIT 2;