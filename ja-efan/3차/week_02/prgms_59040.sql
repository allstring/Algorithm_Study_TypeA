# 241010 
# lv 2
# 고양이와 개는 몇 마리 있을까

SELECT animal_type, COUNT(animal_id) as count
FROM animal_ins 
GROUP BY animal_type
HAVING animal_type in ('Cat', 'Dog')
ORDER BY animal_type;
