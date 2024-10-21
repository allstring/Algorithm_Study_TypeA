-- 코드를 입력하세요
SELECT 
    ROUND(AVG(daily_fee), 0) AS average_fee
FROM 
    car_rental_company_car
GROUP BY 
    car_type
HAVING 
    car_type = 'SUV';