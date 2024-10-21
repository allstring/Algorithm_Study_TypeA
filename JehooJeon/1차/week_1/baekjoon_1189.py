# 1189. 컴백홈

import sys
sys.stdin = open("input.txt", "r")

def dfs(visited, x, y, dist):
    global result
    # 우, 상, 좌, 하 방향
    dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    
    # 거리가 k이고 목적지에 도착할 경우 결과 1 증가
    if dist == k and (x, y) == (0, c-1):
        result += 1
    else:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 좌표 밖으로 벗어날 경우
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            # 이미 방문한 경우
            if visited[nx][ny] == 1:
                continue
            # 벽으로 막힌 경우
            if map[nx][ny] == 'T':
                continue
            
            # nx, ny로 이동하는 경우
            visited[nx][ny] = 1
            dfs(visited, nx, ny, dist + 1)
            # nx, ny로 이동하지 않을 경우
            visited[nx][ny] = 0

# r: 세로 길이, c: 가로 길이, k: 거리
r, c, k = map(int, input().split())
map = [list(input()) for _ in range(r)]
# 방문 여부를 나타낼 visited 배열 생성
visited = [[0] * c for _ in range(r)]

# print(map)
# print(visited)

# 출발 위치 visited 값 1로 설정
visited[r-1][0] = 1
result = 0

# 출발 지점은 왼쪽 아래, 거리는 1로 시작
dfs(visited, r-1, 0, 1)
print(result)