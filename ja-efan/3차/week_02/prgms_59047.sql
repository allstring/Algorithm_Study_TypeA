# 241010
# lv 2
# 이름에 el이 들어가는 동물 찾기 

SELECT animal_id, name 
FROM animal_ins 
WHERE animal_type = "dog" 
    AND (name LIKE "%el%" OR name LIKE "%EL%")
ORDER BY name;