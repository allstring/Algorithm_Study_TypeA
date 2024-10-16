# 241016
# lv 2
# 연도 별 평균 미세먼지 농도 조회하기

SELECT 
    year,
    ROUND(AVG(pm_val1), 2) AS `pm10`,
    ROUND(AVG(pm_val2), 2) AS `pm2.5`
FROM
    (
        SELECT 
            *,
            YEAR(YM) AS `year`
        FROM 
            air_pollution
    ) AS ap
WHERE 1 = 1
    AND location2 = '수원'
GROUP BY 
    year 
ORDER BY 
    year ASC;