# 241016
# lv 2
# 물고기 종류 별 잡은 수 구하기 

SELECT
    COUNT(fi.id) AS `fish_count`,
    fni.fish_name
FROM 
    fish_info AS fi
LEFT JOIN 
    fish_name_info AS fni ON fi.fish_type = fni.fish_type
GROUP BY
    fish_name
ORDER BY 
    fish_count DESC;
        