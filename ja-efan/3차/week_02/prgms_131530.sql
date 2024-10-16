# 241016
# lv 2
# 가격대 별 상품 개수 구하기

SELECT
    price_group,
    COUNT(product_id) AS products
FROM 
    (
        SELECT 
            product_id,
            TRUNCATE(price, -4) AS `price_group`
        FROM 
            product
    ) AS p
GROUP BY
    price_group
ORDER BY 
    price_group ASC;
