from collections import deque
import sys

input = sys.stdin.readline
col, row = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(row)]
visited = [[-1 for _ in range(col)] for _ in range(row)]
fresh_tomato = 0
make_tomato = 0
q = deque()
for i in range(row):
    for j in range(col):
        if tomato[i][j] == 1: #익은 토마토면
            q.append((j, i)) #탐색하기 위해 큐에 넣기
            visited[i][j] = 0
        elif tomato[i][j] == -1: #토마토 없으면
            visited[i][j] = -2 # -2로 표시
        elif tomato[i][j] == 0: #안익은 토마토면
            fresh_tomato += 1
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
max_days = 0 #토마토 다 익는데 걸리는 최대 일수
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < col and 0 <= ny < row:
            if visited[ny][nx] == -1 and tomato[ny][nx] == 0: #방문 안했고 신선한 토마토면
                q.append((nx,ny))
                make_tomato += 1
                visited[ny][nx] = visited[y][x] + 1
                max_days = max(visited[ny][nx], max_days)

if fresh_tomato == make_tomato:
    print(max_days)
else:
    print(-1)
