# 241016
# lv 2
# 월별 잡은 물고기 수 구하기

SELECT 
    COUNT(*) AS `fish_count`,
    MONTH(`time`) AS `month`
FROM
    fish_info
GROUP BY 
    `month`
HAVING -- 생략 가능
    fish_count != 0
ORDER BY
    `month` ASC;