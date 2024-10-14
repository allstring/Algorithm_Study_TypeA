# 241010
# lv 2
# 중성화 여부 파악하기

SELECT 
    animal_id,
    name,
    IF ((sex_upon_intake LIKE "Neutered%" OR sex_upon_intake LIKE "Spayed%"), "O", "X") AS "중성화"
FROM animal_ins
ORDER BY animal_id;