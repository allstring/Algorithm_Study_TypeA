from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]

def find_friends_bfs(i, j, campus, n, m):
    global result
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()

        #경계이거나, 벽이거나, 이미 방문했거나 하면 넘어가기
        if x < 0 or x >= n or y < 0 or y >= m or campus[x][y] == 'X' or campus[x][y] == 'D':
            continue

        # 친구면 -> result +1 후에 이미 방문했으므로 없앰. 'D'로 표시된 것은 이미 확인이 끝난 포지션을 의미함
        if campus[x][y] == 'P':
            result += 1
            campus[x][y] = 'D'

        campus[x][y] = 'D' #확인완료 처리

        #4방향 정의
        dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        #4방향 이동한 곳 모두 enqueue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            queue.append((nx, ny))

start_i = 0
start_j = 0
result = 0

#시작 포지션 찾기
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
           start_i = i
           start_j = j

find_friends_bfs(start_i, start_j, campus, N, M)
print(result if result != 0 else 'TT')