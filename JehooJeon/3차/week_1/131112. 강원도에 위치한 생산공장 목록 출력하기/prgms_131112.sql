-- 코드를 입력하세요
SELECT
    factory_id,
    factory_name,
    address
FROM 
    food_factory
WHERE 
    address LIKE '%강원도%';