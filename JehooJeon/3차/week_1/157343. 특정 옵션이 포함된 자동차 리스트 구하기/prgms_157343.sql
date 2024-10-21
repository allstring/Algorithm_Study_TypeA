-- 코드를 입력하세요
SELECT
    *
FROM 
    car_rental_company_car
WHERE 1 = 1
    AND options LIKE '%네비게이션%'
ORDER BY 
    car_id DESC;