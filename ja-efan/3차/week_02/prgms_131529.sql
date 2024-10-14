# 241010
# lv 2
# 카테고리 별 상품 개수 구하기 

SELECT p.category, COUNT(p.product_id) AS 'product'
FROM (
    SELECT *, SUBSTRING(product_code,1 ,2) AS 'category'
    FROM product 
) AS p
GROUP BY p.category
ORDER BY p.product_code;