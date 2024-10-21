-- 코드를 입력하세요
SELECT
    history_id,
    car_id,
    DATE_FORMAT(start_date, '%Y-%m-%d') AS start_date,
    DATE_FORMAT(end_date, '%Y-%m-%d') AS end_date,
    CASE WHEN DATEDIFF(end_date, start_date) >= 29 THEN '장기 대여'
         ELSE '단기 대여'
    END AS rent_type
FROM 
    car_rental_company_rental_history
WHERE 1 = 1
    AND YEAR(start_date) = 2022
    AND MONTH(start_date) = 9
ORDER BY 
    history_id DESC;