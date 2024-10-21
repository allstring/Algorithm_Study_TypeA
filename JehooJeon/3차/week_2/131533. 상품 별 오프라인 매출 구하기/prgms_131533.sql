-- 코드를 입력하세요
SELECT
    p.product_code,
    SUM(p.price * o.sales_amount) AS sales
FROM 
    product p
JOIN 
    offline_sale o ON p.product_id = o.product_id
GROUP BY 
    p.product_code
ORDER BY 
    SUM(p.price * o.sales_amount) DESC, 
    p.product_code ASC;