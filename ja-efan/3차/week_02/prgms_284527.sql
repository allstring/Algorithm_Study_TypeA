# 241016
# lv 2
# 조건에 맞는 사원 정보 조회하기 

SELECT 
    hg.score,
    he.emp_no,
    he.emp_name,
    he.position,
    he.email
FROM 
    hr_employees AS he 
LEFT JOIN 
    (
        SELECT 
            emp_no,
            SUM(score) AS `score`
        FROM 
            hr_grade
        GROUP BY 
            emp_no
    ) AS hg ON he.emp_no = hg.emp_no
ORDER BY
    score DESC
LIMIT 
    1;
    