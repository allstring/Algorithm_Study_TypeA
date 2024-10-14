# 241010
# lv 2
# 가격이 제일 비싼 식품의 정보 출력하기

# 정렬 후 LIMIT 사용
SELECT product_id, product_name, product_cd, category, price  
FROM food_product
ORDER BY price DESC
LIMIT 1;


# MAX 사용
SELECT product_id, product_name, product_cd, category, price  
FROM food_product
WHERE price = (SELECT MAX(price) FROM food_product);
