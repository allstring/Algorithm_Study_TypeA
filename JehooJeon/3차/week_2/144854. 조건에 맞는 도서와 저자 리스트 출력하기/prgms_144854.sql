-- 코드를 입력하세요
SELECT
    b.book_id,
    a.author_name,
    DATE_FORMAT(b.published_date, '%Y-%m-%d') AS published_date
FROM 
    book b 
LEFT JOIN 
    author a ON b.author_id = a.author_id
WHERE 1 = 1
    AND b.category = "경제"
ORDER BY 
    b.published_date ASC;