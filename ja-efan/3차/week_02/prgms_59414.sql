# 241010
# lv 2
# DATETIME에서 DATE로 형 변환

SELECT 
    animal_id, 
    name, 
    DATE_FORMAT(datetime, "%Y-%m-%d") AS '날짜'
FROM animal_ins
ORDER BY animal_id;