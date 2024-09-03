# 우리집엔 도서관이 있어
# Silver I
# https://www.acmicpc.net/problem/2872

#  책을 정렬할 때 사용할 수 있는 방법은 책 하나를 뺀 다음, 가장 위에 놓는 것이다.

"""
풀이 설명 :
    정렬인줄 알았으나,, 아니었고,,
    현재 책장 상태에서 사전 상 순위가 가장 낮은 책부터 연속된 내림차순 책의 개수를 제외하고는 모두 위로 올려야한다.
    즉, 주어진 입력 값이 정수이므로, 가장 큰 정수 값 (N)을 기준으로 인덱스를 낮춰가며(왼쪽으로)
    '연속된' 내림차순 숫자의 개수를 구해야 한다.
    key point는 '연속된'이다.

"""
def main():
    N = int(input())
    books = [int(input()) for _ in range(N)]

    max_ = N
    max_idx = books.index(max_)
    continuous_cnt = 0  # 연속된 내림차순 숫자 개수 (뽑지 않아도 되는 책의 개수)
    for i in range(max_idx, -1, -1):  # 초기 max_idx기준으로 왼쪽으로 순회
        if books[i] == max_:
            continuous_cnt += 1  # 연속된 내림차순 개수 + 1
            max_ -= 1  # 다음 max값으로 변경

    # 뽑지 않아도 되는 책의 개수를 제외한 값 출력
    print(N - continuous_cnt)



if __name__ == "__main__":
    main()
