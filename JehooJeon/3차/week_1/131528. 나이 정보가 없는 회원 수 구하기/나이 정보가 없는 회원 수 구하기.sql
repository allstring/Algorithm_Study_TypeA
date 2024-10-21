-- 코드를 입력하세요
SELECT
    COUNT(*) AS users
FROM 
    user_info
WHERE 1 = 1
    AND age IS NULL;