# 241016
# lv 2
# 노선별 평균 역 사이 거리 조회하기 

SELECT 
    route, 
    CONCAT(ROUND(SUM(d_between_dist), 1), "km") AS `total_distance`,
    CONCAT(ROUND(AVG(d_between_dist), 2), "km") AS `average_distance`
FROM 
    subway_distance
GROUP BY 
    route 
ORDER BY  -- `total_distance` 컬럼으로 정렬 할 시 문자열 기준 정렬이 되어버림
    ROUND(SUM(d_between_dist), 1) DESC;