# 241014
# lv2 
# 성분으로 구분한 아이스크림 총 주문량

SELECT 
    ii.ingredient_type,
    SUM(total_order) AS 'total_order'
FROM first_half AS fh
INNER JOIN icecream_info AS ii
ON fh.flavor = ii.flavor
GROUP BY ii.ingredient_type
ORDER BY total_order ASC;