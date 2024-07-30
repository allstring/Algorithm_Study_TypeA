# 헌내기는 친구가 필요해
# Silver II
from collections import deque
import sys

inputf = sys.stdin.readline

N, M = map(int, inputf().split())

pos = None
campus = []
for i in range(N):
    campus.append(list(inputf().rstrip()))
    for j in range(M):
        if campus[i][j] == "I":
            pos = (i, j)

# 방문 처리 배열
visited = [[False for _ in range(M)] for _ in range(N)]
# 이동 가능 방향 (상 하 좌 우)
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

p_cnt = 0
queue = deque([pos])
# visited[pos[0]][pos[1]] = True
while queue:
    y, x = queue.popleft()
    # 여기서 visited = True로 줄 경우, 시간 초과 난다.
    # 큐에 들어있는 모든 좌표들이 실제로 POP되지 않는 이상 not visited 상태이기 때문에
    # 너무 많은 좌푣르이 queue에 들어가게 되고, 이로 인해서 시간초과가 발생한다.
    visited[y][x] = True
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx

        # 좌표 유효성 검사
        if 0 <= ny < N and  0 <= nx < M and not visited[ny][nx] and campus[ny][nx] != "X":
            if campus[ny][nx] == "P":
                p_cnt += 1
            queue.append((ny,nx))
            # visited[ny][nx] = True

if p_cnt:
    print(p_cnt)
else :
    print("TT")
