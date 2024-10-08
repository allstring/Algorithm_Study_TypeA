# lv 1
# 조건에 부합하는 중고거래 댓글 조회하기

SELECT
    b.title, 
    b.board_id, 
    r.reply_id, 
    r.writer_id, 
    r.contents, 
    DATE_FORMAT(r.created_date, "%Y-%m-%d") AS created_date
FROM used_goods_board AS b 
    INNER JOIN used_goods_reply AS r
    ON b.board_id = r.board_id
WHERE 
    b.created_date BETWEEN '2022-10-01' AND '2022-10-31' 
    # AND r.created_date BETWEEN '2022-10-01' AND '2022-10-31' 
ORDER BY r.created_date ASC, b.title ASC;