# 1743. 음식물 피하기

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(condo, i, j):

    # 현재 음식물이 있는 위치를 queue에 추가
    queue = deque([(i, j)])
    # 방문한 위치를 나타내는 visited 배열 초기화
    visited = [[0] * m for _ in range(n)]

    # 상, 하, 좌, 우
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 현재 음식물이 존재하는 위치는 1
    visited[i][j] = 1
    # 최초 음식물의 크기는 1
    trash = 1
    
    # 음식물이 존재하지 않을 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 상, 하, 좌, 우 이동하면서 음식물 찾기
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            # 통로 밖으로 벗어나는 경우
            if not (0 <= nx < n and 0 <= ny < m): continue
            # 이미 방문한 위치인 경우
            if visited[nx][ny] == 1: continue
            # 방문한 위치에 쓰레기가 있는 경우
            if condo[nx][ny] == 1:
                # 방문했으므로 visited 값 1
                visited[nx][ny] = 1
                # 현재 위치 queue 추가
                queue.append((nx, ny))
                # 음식물의 크기 +1
                trash += 1
    # 현재 위치의 음식물 크기 반환
    return trash

# n: 세로 길이, m: 가로 길이, k: 음식물 쓰레기의 개수
n, m, k = map(int, input().split())
# 콘도의 통로 배열을 0으로 초기화
condo = [[0] * m for _ in range(n)]
# print(condo)


# 음식물이 떨어진 좌표값 1로 설정
for _ in range(k):
    r, c = map(int, input().split())
    # 인덱스는 0부터 시작하므로 -1
    condo[r-1][c-1] = 1
# print(condo)

# 가장 큰 음식물의 크기 변수 정의
max_trash = 0

# 모든 통로를 순회하면서 쓰레기가 있는 경우 bfs로 음식물의 크기 측정
for i in range(n):
    for j in range(m):
        if condo[i][j] == 1:
            trash = bfs(condo, i, j)
            # 측정한 크기 중에서 가장 큰 음식물 찾기
            max_trash = max(trash, max_trash)

print(max_trash)