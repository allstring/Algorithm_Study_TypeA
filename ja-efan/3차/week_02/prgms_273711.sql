# 241016
# lv 2
# 업그레이드 된 아이템 구하기 

SELECT 
    item_id,
    item_name,
    rarity
FROM 
    item_info
WHERE 
    item_id IN (
        SELECT
            it.item_id AS `upgrade_item_id`
        FROM 
            item_info AS ii
        LEFT JOIN 
            item_tree AS it ON ii.item_id = it.parent_item_id 
        WHERE 1 = 1
            AND ii.rarity = 'RARE'
    )
ORDER BY 
  item_id DESC;