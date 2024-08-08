from collections import deque
def check_scraps(M, N, aisle, i, j):
    scraps_size = 0 #음식물덩어리 사이즈 초기화
    queue = deque([(i,j)])
    while queue:
        x, y = queue.popleft()
        if x<0 or x>=N or y<0 or y>=M or aisle[x][y] == 0: #경계를 벗어나거나 음식물이 아닌 경우
            continue
        aisle[x][y] = 0 #이미 확인한 음식물은 방문처리
        scraps_size += 1 #사이즈 카운팅
        dxy = [(1,0),(0,1),(-1,0),(0,-1)]
        for dx, dy in dxy:
            queue.append((x+dx, y+dy)) #4방향에 대해서 이동
    return scraps_size

N, M, K = map(int, input().split())
aisle = [[0] * M for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    aisle[i-1][j-1] = 1 #음식물의 위치 저장

scraps_list = []
for i in range(N):
    for j in range(M):
        if aisle[i][j] == 1: #발견한 음식물덩어리 위치에서 BFS탐색
            scraps_list.append(check_scraps(M, N, aisle, i, j))

print(max(scraps_list))
