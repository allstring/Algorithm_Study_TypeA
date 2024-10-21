-- 코드를 작성해주세요
SELECT
    CASE WHEN MONTH(differentiation_date) IN (1, 2, 3) THEN '1Q'
         WHEN MONTH(differentiation_date) IN (4, 5, 6) THEN '2Q'
         WHEN MONTH(differentiation_date) IN (7, 8, 9) THEN '3Q'
         WHEN MONTH(differentiation_date) IN (10, 11, 12) THEN '4Q'
    END AS quarter,
    COUNT(id) AS ecoli_count
FROM
    ecoli_data
GROUP BY
    quarter
ORDER BY
    quarter ASC;