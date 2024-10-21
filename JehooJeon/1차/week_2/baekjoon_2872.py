# 2872. 우리집엔 도서관이 있어

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    # N: 책의 개수
    N = int(input())
    # book_list: 책의 순서 리스트
    book_list = [int(input()) for _ in range(N)]
    
    # 가장 큰 숫자를 cnt로 초기화
    cnt = N
    for _ in range(N):
        # 뒤 번호부터 가장 큰 숫자와 비교
        num = book_list.pop()
        # 가장 큰 숫자를 찾았을 경우 -1
        if N == num:
            N -= 1
    
    # 나머지 책을 옮기면 됨
    print(N)

# idea : 어차피 가장 큰 번호의 책은 굳이 옮길 필요 없음
# 또한, 큰 번호부터 순서대로 정렬되어 있는 책들 또한 옮길 필요 없음
# 예를 들면, [1, 3, 2, 4, 5] 순으로 되어있을 경우,
# 3, 4, 5는 순서대로 되어있으므로 1, 2만 한번씩 뽑아서 옮기면 정렬 가능