# 241010
# lv 2
# 입양 시각 구하기 (1)

SELECT 
    hour, 
    COUNT(*) AS `count`
FROM 
    (
        SELECT 
            *, 
            HOUR(datetime) AS `hour`
        FROM 
            animal_outs
    ) AS ao
WHERE 
    hour BETWEEN 9 AND 19
GROUP BY 
    hour
ORDER BY 
    hour ASC;