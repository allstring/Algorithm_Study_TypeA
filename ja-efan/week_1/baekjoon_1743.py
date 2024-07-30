# 음식물 피하기
# Silver I

from collections import deque

# N: 통로의 세로 길이, M: 통로의 가로 길이, K: 음식물 쓰레기의 개수
N, M, K = map(int, input().split())

# 통로
hall = [[0 for _ in range(M)] for _ in range(N)]

# 통로 정보 업데이트
for _ in range(K):
    r, c = map(int, input().split())
    hall[r-1][c-1] = 1

visited = [[False for _ in range(M)] for _ in range(N)]
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
max_size = 0

for row in range(N):
    for col in range(M):
        queue = deque()
        size = 0
        if hall[row][col] == 1 and not visited[row][col]:
            queue.append((row, col))
            visited[row][col] = True
            while queue:
                r, c = queue.popleft()
                size += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and hall[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited[nr][nc] = True

            max_size = max(max_size, size)
print(max_size)
