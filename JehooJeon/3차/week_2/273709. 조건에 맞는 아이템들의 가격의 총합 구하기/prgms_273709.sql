-- 코드를 작성해주세요
SELECT
    SUM(price) AS total_price
FROM 
    item_info
WHERE 1 = 1
    AND rarity = 'LEGEND';