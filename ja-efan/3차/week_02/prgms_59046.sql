# 241014
# lv 2
# 루시와 엘라 찾기 

SELECT 
  animal_id, 
  name, 
  sex_upon_intake
FROM 
  animal_ins 
WHERE 1 = 1 
  AND name IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
ORDER BY 
  animal_id ASC;
