# 241016
# lv 2
# 부모의 형질을 모두 가지는 대장균 찾기 

SELECT 
    ed.id AS `id`,
    ed.genotype AS `genotype`,
    ped.genotype AS `parent_genotype`
FROM 
    ecoli_data AS ed
LEFT JOIN -- parent_ecoli_data
    (
        SELECT 
            id,
            genotype 
        FROM 
            ecoli_data
    ) AS ped ON ed.parent_id = ped.id
WHERE 1 = 1
    AND (ed.genotype & ped.genotype) = ped.genotype -- 비트 연산 
ORDER BY 
    ed.id ASC;