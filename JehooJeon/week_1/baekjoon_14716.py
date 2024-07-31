# 14716. 현수막

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(banner, st_x, st_y):

    # 상, 하, 좌, 우, 대각선
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    visited = [[0] * n for _ in range(m)]

    queue = deque([(st_x, st_y)])

    while queue:
        x,  y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if banner[nx][ny] == 0:
                continue

            banner[nx][ny] = 0
            queue.append((nx, ny))

# m, n: 현수막의 크기
# 1 <= m, n <= 250
m, n = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(m)]
result = 0

for i in range(m):
    for j in range(n):
        if banner[i][j] == 1:
            bfs(banner, i, j)
            result += 1

print(result)