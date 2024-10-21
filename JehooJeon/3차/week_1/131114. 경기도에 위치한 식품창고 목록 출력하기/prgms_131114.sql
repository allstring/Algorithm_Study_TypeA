-- 코드를 입력하세요
SELECT
    warehouse_id,
    warehouse_name,
    address,
    CASE WHEN freezer_yn IS NULL THEN 'N'
         ELSE freezer_yn
    END AS freezer_yn
FROM 
    food_warehouse
WHERE 1 = 1
    ANd warehouse_name LIKE '%경기%'
ORDER BY 
    warehouse_id ASC;