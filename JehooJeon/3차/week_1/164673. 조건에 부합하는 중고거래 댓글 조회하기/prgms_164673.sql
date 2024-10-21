-- 코드를 입력하세요
SELECT
    b.title,
    b.board_id,
    r.reply_id,
    r.writer_id,
    r.contents,
    DATE_FORMAT(r.created_date, '%Y-%m-%d') AS created_date
FROM 
    used_goods_board b 
JOIN used_goods_reply r ON b.board_id = r.board_id
WHERE 1 = 1
    AND YEAR(b.created_date) = 2022
    AND MONTH(b.created_date) = 10
ORDER BY 
    created_date ASC, 
    title ASC;