# lv 1
# 특정 형질을 가지는 대장균 찾기

# 2번 형질을 보유하지 않는다 -> GENOTYPE & 2 = 0 
# 1번 형질 혹은 3번 형질을 보유한다 -> GENOTYPE & 1 = 1 or GENOTYPE & 4 = 4
SELECT COUNT(id) as 'count'
FROM ecoli_data 
WHERE (genotype & 2) = 0 
    AND (genotype & 1 = 1 OR genotype & 4 = 4); 
