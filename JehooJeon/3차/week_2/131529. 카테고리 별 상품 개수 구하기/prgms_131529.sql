-- 코드를 입력하세요
SELECT
    SUBSTRING(product_code, 1, 2) AS category,
    COUNT(*) AS products
FROM 
    product
GROUP BY 
    category;