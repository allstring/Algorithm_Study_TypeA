# 넴모넴모
# Gold V
# Backtracking
"""
풀이 설명:
    DFS로 완전탐색
    (r,c) 좌표에 넴모를 위치시키기 전에 (왼쪽 상단, 왼쪽, 위쪽)에 넴모가 존재하는지를 체크해서 가지치기

"""


def dfs(curr_pos):
    global cnt, grid
    # 좌표 끝까지 돈 경우
    if curr_pos[0] == N:
        cnt += 1  # 개수 추가
        return

    # 현재 좌표
    curr_r = curr_pos[0]
    curr_c = curr_pos[1]

    # 다음 좌표
    next_r = curr_r + (curr_c + 1) // M
    next_c = (curr_c + 1) % M

    # 현재 위치에 넴모가 존재하지 않는 경우: 다음 좌표로 넘어감
    dfs((next_r, next_c))

    # pruning : 현재 좌표에 넴모를 놓기 전에 가지치기
    # 현재 위치에 넴모가 존재하는 경우를 탐색하기 전에
    # 왼쪽 상단 대각선, 왼쪽, 위 방향에 넴모가 존재하는 지 확인
    check_sum = 0
    for dr, dc in check_direction:
        check_r = curr_r + dr
        check_c = curr_c + dc
        check_sum += grid[check_r][check_c]
    # check_sum이 3 -> 현재 좌표에 넴모를 위치할 경우 2x2 클러스터 형성 됨
    if not check_sum == 3:
        # 넴모 추가
        grid[curr_r][curr_c] = 1
        # dfs recursion
        dfs((next_r, next_c))
        # 넴모 원복
        grid[curr_r][curr_c] = 0


def main():
    dfs((0, 0))
    print(cnt)


if __name__ == "__main__":
    check_direction = [[-1, -1], [-1, 0], [0, -1]]
    cnt = 0
    N, M = map(int, input().split())
    grid = [[0 for _ in range(M)] for _ in range(N)]
    main()

