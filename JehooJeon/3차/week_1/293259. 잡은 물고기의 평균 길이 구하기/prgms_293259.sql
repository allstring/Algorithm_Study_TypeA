-- 코드를 작성해주세요

SELECT
    ROUND(AVG(length), 2) AS average_length
FROM (SELECT
        CASE WHEN length IS NULL THEN 10
             ELSE length
        END AS length
      FROM fish_info) AS adjusted_lengths;