# lv 1
# 잡은 물고기의 평균 길이 구하기 

SELECT 
    ROUND(AVG(IFNULL(length, 10)), 2) AS average_length
FROM fish_info;


