-- 코드를 입력하세요
SELECT
    animal_id,
    name,
    sex_upon_intake
FROM 
    animal_ins
WHERE 1 = 1
    AND name IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty');