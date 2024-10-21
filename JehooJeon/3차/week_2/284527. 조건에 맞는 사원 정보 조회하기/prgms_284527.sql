-- 코드를 작성해주세요
SELECT
    SUM(hg.score) AS score,
    he.emp_no,
    he.emp_name,
    he.position,
    he.email
FROM
    hr_employees he
LEFT JOIN
    hr_grade hg ON he.emp_no = hg.emp_no
GROUP BY
    he.emp_no
ORDER BY
    score DESC
LIMIT 1;