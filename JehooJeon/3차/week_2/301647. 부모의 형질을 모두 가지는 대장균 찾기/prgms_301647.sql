-- 코드를 작성해주세요
SELECT
    ed1.id,
    ed1.genotype,
    ed2.genotype AS parent_genotype
FROM
    ecoli_data ed1
LEFT JOIN
    ecoli_data ed2 ON ed1.parent_id = ed2.id
WHERE 1 = 1
    AND ed1.genotype & ed2.genotype = ed2.genotype
ORDER BY
    ed1.id ASC