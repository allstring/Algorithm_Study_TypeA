# 241016
# lv 2
# ROOT 아이템 구하기 

SELECT
    ii.item_id,
    ii.item_name
FROM 
    item_info AS ii
LEFT JOIN
    item_tree AS it ON ii.item_id = it.item_id
WHERE 1 = 1
    AND it.parent_item_id IS NULL
ORDER BY 
    item_id ASC;