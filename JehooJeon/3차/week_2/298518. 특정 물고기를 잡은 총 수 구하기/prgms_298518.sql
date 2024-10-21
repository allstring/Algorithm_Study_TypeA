-- 코드를 작성해주세요
SELECT 
    COUNT(*) AS fish_count
FROM
    fish_info fi
LEFT JOIN
    fish_name_info fni ON fi.fish_type = fni.fish_type
WHERE 1 = 1
    AND fni.fish_name IN ('BASS', 'SNAPPER');