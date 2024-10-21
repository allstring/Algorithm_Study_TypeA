-- 코드를 작성해주세요
SELECT
    COUNT(*) AS fish_count,
    MONTH(time) AS month
FROM 
    fish_info
GROUP BY
    MONTH(time)
ORDER BY
    month ASC;