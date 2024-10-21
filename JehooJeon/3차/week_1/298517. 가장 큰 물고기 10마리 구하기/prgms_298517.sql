-- 코드를 작성해주세요
SELECT
    id,
    length
FROM 
    fish_info
ORDER BY 
    length DESC, 
    id ASC
LIMIT 10;