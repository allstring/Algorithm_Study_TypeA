# 241016
# lv 2
# 특정 물고기를 잡은 총 수 구하기 

SELECT
    COUNT(*) AS `fish_count`
FROM
    fish_info AS fi
LEFT JOIN 
    fish_name_info AS fni ON fi.fish_type = fni.fish_type
WHERE 1 = 1
    AND fni.fish_name IN ("BASS", "SNAPPER");