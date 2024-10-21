-- 코드를 작성해주세요
SELECT
    COUNT(*) AS fish_count,
    fni.fish_name
FROM
    fish_info fi
LEFT JOIN
    fish_name_info fni ON fi.fish_type = fni.fish_type
GROUP BY
    fni.fish_name
ORDER BY
    fish_count DESC;