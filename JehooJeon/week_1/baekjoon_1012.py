# 1012. 유기농 배추

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(arr, x, y):
    arr[x][y] = 0

    queue = deque([(x, y)])

    while queue:
        fx, fy = queue.popleft()

        # 상, 하, 좌, 우
        dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for dx, dy in dxy:
            nx, ny = fx + dx, fy + dy

            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))

T = int(input())

for _ in range(T):
    # m: 배추밭의 가로길이, n: 배추밭의 세로길이, k: 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    # print(arr)
    field_cnt = 0

    for x in range(m):
        for y in range(n):
            if arr[x][y] == 1:
                bfs(arr, x, y)
                field_cnt += 1

    print(field_cnt)