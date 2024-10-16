# 241010
# lv 2
# 조건에 맞는 아이템들의 가격의 총합 구하기

SELECT 
  SUM(price) AS `total_price`
FROM 
  item_info
WHERE 1 = 1 
  rarity = 'LEGEND';