-- 코드를 입력하세요
SELECT
    animal_id,
    name
FROM 
    animal_ins
WHERE 1 = 1
    AND animal_type = 'Dog'
    AND name LIKE '%el%'
ORDER BY 
    name ASC;