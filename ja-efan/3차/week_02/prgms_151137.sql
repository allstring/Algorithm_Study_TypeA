# 241014
# lv2
# 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기 

SELECT car_type, count(car_id) as 'cars'
FROM car_rental_company_car
WHERE options REGEXP("통풍시트|열선시트|가죽시트")
GROUP BY car_type
ORDER BY car_type;