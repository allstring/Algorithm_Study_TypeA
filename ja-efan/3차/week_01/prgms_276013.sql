# lv 1
# Python 개발자 찾기 

SELECT 
    id, 
    email, 
    first_name, 
    last_name
FROM developer_infos
WHERE 
    skill_1 = 'PYTHON'
    OR skill_2 = 'PYTHON' 
    OR skill_3 = 'PYTHON'
ORDER BY id ASC;