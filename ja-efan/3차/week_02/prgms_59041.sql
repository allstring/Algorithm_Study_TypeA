# 241010
# lv 2
# 동명 동물 수 찾기 

SELECT 
  name, 
  COUNT(name) AS `count`
FROM 
  animal_ins 
GROUP BY 
  name
HAVING 
  COUNT(name) >= 2
ORDER BY 
  name ASC;