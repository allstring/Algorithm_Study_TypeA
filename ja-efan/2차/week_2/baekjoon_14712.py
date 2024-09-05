# 넴모넴모(Easy)
# Gold V

from itertools import combinations

"""
격자판의 비어 있는 칸을 임의로 골라 “넴모”를 하나 올려놓거나,
“넴모”가 올라간 칸 네 개가 2 × 2 사각형을 이루는 부분을 찾아 그 위에 있는 “넴모”들을 모두 없애는 것

-> 넴모를 없애고 싶은데, 없앨 수 있는 넴모가 없다
-> 2x2 넴모 군집이 없다

행의 개수 N, 열의 개수 M(1 ≤ N, M ≤ 25, 1 ≤ N × M ≤ 25)
"""


def count_case(coordinations_list):
    global grid

    for coordinations in coordinations_list:
        for coord in coordinations:
            grid[coord[0]][coord[1]] = 1

    cnt = 0
    for r in range(N - 2):
        for c in range(M - 2):
            if sum(grid[r, c] + grid[r + 1][c] + grid[r][c + 1] + grid[r + 1][c + 1]) == 4:
                continue

            cnt += 1
    return cnt


def main():
    global N, M
    N, M = map(int, input().split())
    # 행 혹은 열의 길이가 1인 경우 2x2 넴모 배치가 불가능하다.
    if N == 1:
        print(2 ** M)
        return
    elif M == 1:
        print(2 ** N)
        return

    coordinations = list()
    for r in range(N):
        for c in range(M):
            coordinations.append((r, c))

    print(coordinations)

    result = 0
    for i in range(2, N * M):
        print(i)
        nemmo_pos = list(combinations(coordinations, i))
        print(nemmo_pos)
        print("*"*50)

        # result += count_case(nemmo_pos)

    print(result)


if __name__ == "__main__":
    # n = 25
    # sum_ = 0
    # for i in range(1, 26):
    #     len_ = len(list(combinations(range(25), i)))
    #     print(len_)
    #     sum_ += len_
    #
    # print(sum_)
    N, M = 0, 0
    grid = None
    main()
