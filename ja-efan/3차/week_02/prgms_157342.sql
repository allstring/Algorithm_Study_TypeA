# 241016 
# lv 2
# 자동차 평균 대여 기간 구하기 

SELECT
    car_id,
    ROUND(AVG(DATEDIFF(end_date, start_date) + 1), 1) AS `average_duration`
FROM
    car_rental_company_rental_history
GROUP BY 
  car_id
HAVING 1 = 1
    AND average_duration >= 7
ORDER BY 
    average_duration DESC,
    car_id DESC;