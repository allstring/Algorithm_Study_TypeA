# 241016
# lv 2
# 재구매가 일어난 상품과 회원 리스트 구하기 

SELECT
    user_id, 
    product_id
FROM
    online_sale
GROUP BY 
    user_id, 
    product_id
HAVING 1 = 1
    AND COUNT(online_sale_id) > 1
ORDER BY 
    user_id ASC, 
    product_id DESC;