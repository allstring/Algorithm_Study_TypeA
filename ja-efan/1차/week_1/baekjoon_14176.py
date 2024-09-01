from collections import deque
import sys

input = sys.stdin.read

data = input().split()

M, N = int(data[0]), int(data[1])
placard = []
idx = 2
for _ in range(M):
    placard.append(list(map(int, data[idx:idx + N])))
    idx += N

# 방문 처리 배열
visited = [[False] * N for _ in range(M)]

# 현재 좌표 기준 8방향에 대한 방향 정보
directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

letter_cnt = 0
# 모든 좌표에 대하여 순회
for i in range(M):
    for j in range(N):
        if placard[i][j] == 1 and not visited[i][j]:
            queue = deque([(i, j)])
            while queue:
                y, x = queue.popleft()  # 좌표 하나 pop
                visited[y][x] = True  # 현재 좌표 방문 처리

                # 현재 좌표 기준 8방향에 대한 순회
                for dy, dx in directions:
                    ny = y + dy  # 다음 행
                    nx = x + dx  # 다음 열

                    # 좌표 유효성 검사
                    if 0 <= ny < M and 0 <= nx < N and placard[ny][nx] == 1 and not visited[ny][nx]:
                        queue.append((ny,nx))

            letter_cnt += 1

print(f"{letter_cnt}")