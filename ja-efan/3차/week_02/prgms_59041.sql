# 241010
# lv 2
# 동명 동물 수 찾기 

SELECT name, count(name) as count
FROM animal_ins 
GROUP BY name
HAVING count(name) >= 2
ORDER BY name;