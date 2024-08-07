# 컴백홈
# https://www.acmicpc.net/problem/1189

R, C, K = map(int, input().split())

# 집가는 길
map_ = [list(input().rstrip()) for _ in range(R)]
# 방문 체크
visited = [[False for _ in range(C)] for _ in range(R)]
# 진행 가능 방향
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# 집 가는 방법 가짓 수
cnt = 0
# 한수 초기 좌표 (왼쪽 아래 점)
init_r, init_c = R-1, 0
# 초기 위치 방문 처리
visited[init_r][init_c] = True
# 이동 거리
init_dist = 1
# 집 좌표
hr, hc = 0, C-1


def dfs(r, c, dist):
    global cnt
    if dist == K and (r == hr and c == hc):  # K 거리 움직였을 때, 집인 경우
        cnt += 1  # 카운트 + 1 해주고 반환
        return
    for dr, dc in directions:  # 현재 위치에서 4 방향 순회
        nr, nc = r + dr, c + dc  # 다음 좌표
        # 좌표 유효성 검사
        if 0 <= nr < R and 0 <= nc < C and map_[nr][nc] != 'T' and not visited[nr][nc]:
            visited[nr][nc] = True  # 다음 좌표 방문 처리
            dfs(nr, nc, dist+1)  # 다음 좌표 기준 dfs recursion
            visited[nr][nc] = False  # 다음 좌표 방문 처리 원복


dfs(init_r, init_c, init_dist)
print(cnt)

