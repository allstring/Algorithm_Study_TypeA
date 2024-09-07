from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for dir in dxy:
            nx = x + dir[0]
            ny = y + dir[1]
            
                # 배열 범위 내에 있고, 익지 않은 토마토면
            if 0 <= nx < row and 0 <= ny < col and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1  # 익은 날 ++
                queue.append((nx, ny))


col, row = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(row)]

dxy=[[-1,0],[1,0],[0,-1],[0,1]] # 상, 하, 좌, 우

queue = deque()

# 익은 토마토 좌표 큐 삽입
for i in range(row):
    for j in range(col):
        if tomatos[i][j] == 1:  # 익은 토마토
            queue.append((i, j))

bfs()

if any(0 in row for row in tomatos): # 익지 않은 토마토 있으면 -1 출력
    print(-1)
else: # 시작을 1로 했으니 max_days에서 1빼고 출력
    max_days = max(max(row) for row in tomatos)
    print(max_days - 1)

# max_days = 0
# for i in range(row):
#     for j in range(col):
#         if tomatos[i][j] == 0:
#             print(-1)
#             exit()
#         max_days = max(max_days, tomatos[i][j])

# print(max_days - 1)
