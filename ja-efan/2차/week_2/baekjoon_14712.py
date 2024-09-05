# 넴모넴모(Easy)
# Gold V
# Combination

from itertools import combinations
from pprint import pprint

"""
격자판의 비어 있는 칸을 임의로 골라 “넴모”를 하나 올려놓거나,
“넴모”가 올라간 칸 네 개가 2 × 2 사각형을 이루는 부분을 찾아 그 위에 있는 “넴모”들을 모두 없애는 것

-> 넴모를 없애고 싶은데, 없앨 수 있는 넴모가 없다
-> 2x2 넴모 군집이 없다

행의 개수 N, 열의 개수 M(1 ≤ N, M ≤ 25, 1 ≤ N × M ≤ 25)
"""


def count_case(coordination_list):
    global grid

    cnt = 0
    for coordinations in coordination_list:
        for coord in coordinations:
            grid[coord[0]][coord[1]] = 1

        for r in range(N - 2):
            for c in range(M - 2):
                if sum(grid[r][c] + grid[r + 1][c] + grid[r][c + 1] + grid[r + 1][c + 1]) == 4:
                    continue
        pprint(grid)
        cnt += 1
    return cnt


def count(coordination_list):
    global grid
    _next = False
    cnt = 0
    while coordination_list:
        _next=False
        nemmo_pos = set(coordination_list.pop())
        # 넴모 배치
        for r in range(N):
            for c in range(M):
                if (r,c) in nemmo_pos:
                    grid[r][c] = 1
                else:
                    grid[r][c] = 0

        for r in range(N-1):
            for c in range(M-1):
                if (grid[r][c] + grid[r + 1][c] + grid[r][c + 1] + grid[r + 1][c + 1]) == 4:
                    _next = True
                    break
            if _next: break
        if _next: continue
        cnt += 1
    return cnt


def main():
    global N, M, grid
    N, M = map(int, input().split())
    # 행 혹은 열의 길이가 1인 경우 2x2 넴모 배치가 불가능하다.
    grid = [[0 for _ in range(M)] for _ in range(N)]
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

    nemmo_pos = []
    for i in range(2, N * M):
        nemmo_pos.extend(list(combinations(coordinations, i)))

    result = count(nemmo_pos)
    # 한 칸에만 넴모가 존재하는 경우
    result += N*M
    # 아무 칸에도 넴모가 없는 경우
    result += 1
    print(result)


if __name__ == "__main__":
    import time
    start = time.time()
    N, M = 0, 0
    grid = list()
    main()
    end = time.time()
    print(f"{end - start:.5f} sec")
