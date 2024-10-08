# lv 1
# 가장 큰 물고기 10마리 구하기

SELECT id, length
FROM FISH_INFO
ORDER BY length DESC, id ASC
LIMIT 10;