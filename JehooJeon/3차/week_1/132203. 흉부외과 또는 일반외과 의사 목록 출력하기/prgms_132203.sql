-- 코드를 입력하세요
SELECT
    dr_name,
    dr_id,
    mcdp_cd,
    DATE_FORMAT(hire_ymd, '%Y-%m-%d') AS hire_ymd
FROM 
    doctor
WHERE 1 = 1
    AND mcdp_cd IN ('CS', 'GS')
ORDER BY 
    hire_ymd DESC, 
    dr_name ASC;