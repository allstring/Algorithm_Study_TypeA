from collections import deque

N = int(input())
books = [int(input()) for _ in range(N)]

max_book = max(books)
max_idx = books.index(max_book)

#LIS알고리즘과 다른 점
#단순 증가가 아니라 연속 증가여야 함!

sorted_sub = 1
for i in range(max_idx-1, -1, -1):
    if books[i] + 1 == max_book:
        max_book = books[i]
        sorted_sub += 1
print(N-sorted_sub)
