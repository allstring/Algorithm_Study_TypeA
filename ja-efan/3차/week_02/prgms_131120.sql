# 241014
# lv 2
# 3월에 태어난 여성 회원 목록 출력하기

SELECT
    member_id, 
    member_name,
    gender,
    DATE_FORMAT(date_of_birth, "%Y-%m-%d") AS 'date_of_birth'
FROM 
    member_profile
WHERE 1 = 1
    AND gender = 'W'
    AND MONTH(date_of_birth) = 3
    AND tlno IS NOT NULL
ORDER BY 
    member_id ASC;