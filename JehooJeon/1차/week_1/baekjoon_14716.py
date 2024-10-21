# 14716. 현수막

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(banner, st_x, st_y):

    # 상, 하, 좌, 우, 대각선
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    # 방문한 위치를 나타내는 배열 정의
    visited = [[0] * n for _ in range(m)]

    # 현재 글자가 있는 위치 queue에 추가
    queue = deque([(st_x, st_y)])

    # 인접한 글자가 없을 때까지 반복
    while queue:
        x,  y = queue.popleft()
        
        # 상, 하, 좌, 우, 대각선 이동하면서 확인
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            # 현수막을 벗어날 경우
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            # 현수막에서 글자가 아닌 부분일 경우
            if banner[nx][ny] == 0:
                continue
            
            # 현수막에서 인접한 부분이 글자인 경우
            # 현수막 값을 0으로 바꾸고 하나의 글자로 생각
            banner[nx][ny] = 0
            # 현재 글자가 있는 부분을 queue에 추가
            queue.append((nx, ny))

# m, n: 현수막의 크기
# 1 <= m, n <= 250
m, n = map(int, input().split())
# 현수막 배열 값 받아오기
banner = [list(map(int, input().split())) for _ in range(m)]
# 글자의 개수 변수 정의
result = 0

# 현수막을 순회
for i in range(m):
    for j in range(n):
        # 현수막에 글자가 있는 경우
        if banner[i][j] == 1:
            # bfs를 통해 인접하여 있는 글자 확인
            bfs(banner, i, j)
            # 글자 수 추가
            result += 1

print(result)