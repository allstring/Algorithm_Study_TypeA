# 배열 돌리기 4
# Gold IV
# https://www.acmicpc.net/problem/17406


def cal_matrix_value(matrix):
    min_ = 10000
    for row in matrix:
        min_ = min(min_, sum(row))

    return min_


def matrix_rotate(matrix, r, c, s):
    """
    (r-s, c-s)를 좌측 상단, (r+s, c+s)를 우측 하단으로 하는
    matrix의 submatrix(정사각형)를 시계 방향으로 한 칸씩 돌린다.
    :param matrix: 피연산자(행렬)
    :param r:
    :param c:
    :param s:
    :return:
    """
    N = len(matrix)
    M = len(matrix[0])
    left_top = (r-s-1, c-s-1)
    # left_bottom = c+s-1
    # right_top = c-s-1
    right_bottom = (r+s-1, c+s-1)
    sub_N = right_bottom[0] - left_top[0]
    # (r-s, c-s)를 좌측 상단, (r+s, c+s)를 우측 하단으로 하는 sub-matrix
    submatrix = [[0 for _ in range(sub_N)] for _ in range(sub_N)]
    for i in range(N):
        if i < left_top[0]  or i > right_bottom[0]:
            continue
        for j in range(M):
            if j < left_top[1] or j > right_bottom[1]:
                continue

    pass


def main():
    # N, M: 배열 크기, K: 회전 연산 개수
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]  # 배열 A
    rotate_info = [list(map(int, input().split())) for _ in range(K)]  # K개의 회전 연산 정보(r,c,s)


if __name__ == "__main__":
    main()