-- 코드를 입력하세요
SELECT date_format(DATETIME, "%H") AS HOUR, COUNT(date_format(DATETIME, "%H")) AS COUNT
FROM ANIMAL_OUTS
WHERE date_format(DATETIME, "%H") >= 9 AND
date_format(DATETIME, "%H") < 20
GROUP BY date_format(DATETIME, "%H")
ORDER BY HOUR