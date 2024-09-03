# 토마토
# Gold IV

import sys
sys.setrecursionlimit(10000)
def is_valid(pos):
    r, c = pos[0], pos[1]
    # 좌표 유효성 검사
    if r < 0 or r >= N or c < 0 or c >= M:
        return False
    # # 방문 췍
    # if visited[r][c]:
    #     return False
    # 토마토 췍
    if box[r][c] != 0:
        return False
    return True


def dfs(coord_list, day):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 익은 토마토가 영향을 끼치는 방향

    # 어제 익은 토마토가 없다
    # -> 이미 모든 토마토가 익었다.
    # or 익지 못하는 토마토가 존재한다. (사각지대 토마토)
    if not coord_list:
        # 이미 모든 토마토가 익었다.
        if sum([sum(row) for row in box]) == (N*M)-2*EMPTY:
            print(day-1)
            return
        # 익지 못하는 토마토가 존재
        print(-1)
        return

    # 오늘 익은 토마토들의 좌표
    new_ripe_tomato = []
    for ripe_tomato in coord_list:  # 어제 익은 토마토 좌표들
        cr, cc = ripe_tomato[0], ripe_tomato[1]
        for dr, dc in directions:  # 인접한 4 방향에 대해서 확인
            nr, nc = cr + dr, cc + dc   # 인접 좌표
            if is_valid((nr, nc)):
                # visited[nr][nc] = True  # 방문 췍
                box[nr][nc] = 1
                new_ripe_tomato.append((nr, nc))  # 오늘 익은 토마토 좌표 추가

    day += 1
    return dfs(coord_list=new_ripe_tomato, day=day)


def main():
    global N, M, box, EMPTY
    # global visited

    M, N = map(int, input().split())  # N x M 상자의 크기 [2, 1000]
    box = [list(map(int, input().split())) for _ in range(N)]

    # 저장될 때부터 모든 토마토가 익어있는 상태 -> 바로 컽
    if sum([sum(row) for row in box]) == N*M:
        print(0)
        return

    # visited = [[False for _ in range(M)] for _ in range(N)]
    ripe_tomatoes = list()  # 익은 토마토들의 좌표
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                ripe_tomatoes.append((r, c))
            elif box[r][c] == -1:
                EMPTY += 1

    dfs(coord_list=ripe_tomatoes, day=0)


if __name__ == "__main__":
    N, M =  0, 0
    # visited = []
    box = []
    EMPTY = 0
    main()