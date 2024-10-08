# lv 1
# 자동차 대여 기록에서 장기/단기 대여 구분하기

WITH cte1 AS (
    SELECT 
    *,
    DATEDIFF(end_date, start_date)+1 AS rental_date
    FROM car_rental_company_rental_history
    WHERE start_date 
        BETWEEN "2022-09-01" AND "2022-09-30"
)
SELECT 
    history_id,
    car_id,
    DATE_FORMAT(start_date, "%Y-%m-%d") AS start_date,
    DATE_FORMAT(end_date, "%Y-%m-%d") AS end_date,
    IF(rental_date >= 30, "장기 대여", "단기 대여") AS rent_type
FROM cte1
ORDER BY history_id DESC;
    