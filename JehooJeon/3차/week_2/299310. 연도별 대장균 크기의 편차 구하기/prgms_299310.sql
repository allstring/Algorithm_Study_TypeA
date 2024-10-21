-- 코드를 작성해주세요
SELECT
    YEAR(ed.differentiation_date) AS year,
    ABS(max_size - ed.size_of_colony) AS year_dev,
    id
FROM
    ecoli_data ed
LEFT JOIN
    (SELECT
        YEAR(ed.differentiation_date) AS year,
        MAX(ed.size_of_colony) AS max_size
     FROM
        ecoli_data ed
     GROUP BY 
        YEAR(ed.differentiation_date)) AS med ON YEAR(ed.differentiation_date) = med.year
ORDER BY
    year ASC,
    year_dev ASC;