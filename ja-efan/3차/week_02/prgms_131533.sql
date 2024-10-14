# 241014 
# lv 2
# 상품 별 오프라인 매출 구하기

SELECT
    p.product_code,
    (p.price * os.total_sales_amount) AS 'sales'
FROM product AS p
INNER JOIN (
    SELECT product_id, SUM(sales_amount) AS total_sales_amount
    FROM offline_sale 
    GROUP BY product_id
) AS os
ON p.product_id = os.product_id
GROUP BY p.product_code
ORDER BY sales DESC, product_code ASC;