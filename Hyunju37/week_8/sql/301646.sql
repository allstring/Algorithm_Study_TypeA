-- 2번 형질을 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE >> 1) & 1 = 0 AND ((GENOTYPE) & 1 = 1 OR (GENOTYPE >> 2) & 1 = 1)
