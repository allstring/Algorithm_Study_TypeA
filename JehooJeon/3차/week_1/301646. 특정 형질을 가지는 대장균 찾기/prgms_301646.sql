-- 코드를 작성해주세요
SELECT
    COUNT(*) AS count
FROM 
    ecoli_data
WHERE 1 = 1
    AND (genotype & 2) != 2
    AND ((genotype & 4) = 4 OR (genotype & 1) = 1)