-- 코드를 입력하세요
SELECT
    COUNT(*) AS users
FROM 
    user_info
WHERE 1 = 1
    AND joined BETWEEN '2021-01-01' AND '2021-12-31'
    AND age BETWEEN 20 AND 29;