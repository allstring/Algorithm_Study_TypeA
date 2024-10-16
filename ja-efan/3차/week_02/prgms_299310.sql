# 241016
# lv 2
# 연도별 대장균 크기의 편차 구하기 

SELECT 
    ed.year,
    (my.max_size_of_year - ed.size_of_colony) AS year_dev,
    id 
FROM    
    (
        SELECT 
            *,
            YEAR(differentiation_date) AS `year`
        FROM 
            ecoli_data 
    ) AS ed
LEFT JOIN 
    (
        SELECT
            YEAR(differentiation_date) AS `year`,
            MAX(size_of_colony) AS `max_size_of_year`
        FROM 
            ecoli_data
        GROUP BY 
            year
    ) AS my ON ed.year = my.year
ORDER BY 
    year ASC,   
    year_dev ASC;