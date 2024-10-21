# 1012. 유기농 배추

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(arr, x, y):
    # 현재 배추가 있는 위치 방문했으므로 0으로 변경
    arr[x][y] = 0

    # 방문한 위치 queue에 추가
    queue = deque([(x, y)])

    # 더 이상 배추가 있는 위치가 없을 때까지 반복
    while queue:
        # queue에서 현재 방문한 위치 
        fx, fy = queue.popleft()

        # 상, 하, 좌, 우
        dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # 상, 하, 좌, 우 움직이면서 확인
        for dx, dy in dxy:
            nx, ny = fx + dx, fy + dy
            
            # 배추밭 범위 벗어날 경우
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            # 배추가 심어져 있지 않을 경우
            if arr[nx][ny] == 0:
                continue
            
            # 배추가 심어져 있을 경우
            # 배추가 있는 위치 0으로 변경 후 queue에 추가
            arr[nx][ny] = 0
            queue.append((nx, ny))

T = int(input())

for _ in range(T):
    # m: 배추밭의 가로길이, n: 배추밭의 세로길이, k: 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    # 배추밭 배열을 0으로 초기화
    arr = [[0] * n for _ in range(m)]

    # 배추가 심어져 있는 위치를 받아 값을 1로 변경
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    # print(arr)
    # 배추흰지렁이 지역 개수 변수 0으로 정의
    field_cnt = 0

    # 배추밭 순회하면서 배추가 심어져 있는 곳에서 지역 개수 +1
    # 이동할 수 있는 배추 지역을 bfs로 확인
    for x in range(m):
        for y in range(n):
            if arr[x][y] == 1:
                bfs(arr, x, y)
                field_cnt += 1

    print(field_cnt)
