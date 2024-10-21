-- 코드를 입력하세요
SELECT
    a.flavor
FROM 
    first_half AS a 
LEFT JOIN
    icecream_info AS b ON a.flavor = b.flavor
WHERE 1 = 1
    AND a.total_order > 3000
    AND b.ingredient_type = 'fruit_based'
ORDER BY 
    a.total_order DESC;