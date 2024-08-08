# 2872. 우리집엔 도서관이 있어

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    # N: 책의 개수
    N = int(input())
    # book_list: 책의 순서 리스트
    book_list = [int(input()) for _ in range(N)]

    cnt = 1
    for book in book_list:
        if book == cnt:
            cnt += 1

    print(N - cnt + 1)