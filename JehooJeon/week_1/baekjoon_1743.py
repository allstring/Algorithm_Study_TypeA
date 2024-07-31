# 1743. 음식물 피하기

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(condo, i, j):

    queue = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    # 상, 하, 좌, 우
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited[i][j] = 1
    # 최초 음식물의 크기는 1
    trash = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m): continue
            if visited[nx][ny] == 1: continue
            if condo[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                trash += 1
    return trash

# n: 세로 길이, m: 가로 길이, k: 음식물 쓰레기의 개수
n, m, k = map(int, input().split())
condo = [[0] * m for _ in range(n)]
# print(condo)


# 음식물이 떨어진 좌표값 1로 설정
for _ in range(k):
    r, c = map(int, input().split())
    # 인덱스는 0부터 시작하므로 -1
    condo[r-1][c-1] = 1
# print(condo)

max_trash = 0

for i in range(n):
    for j in range(m):
        if condo[i][j] == 1:
            trash = bfs(condo, i, j)
            max_trash = max(trash, max_trash)

print(max_trash)