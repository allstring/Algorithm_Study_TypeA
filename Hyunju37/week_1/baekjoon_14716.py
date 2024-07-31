from collections import deque

#BFS 함수
#DFS 아닌 BFS로 푼 이유??
#배추 문제보다 '이웃'의 범위가 넓어서(대각선을 포함하므로)
#재귀호출을 이용하는 DFS 쓰면 시간복잡도가 커질 것이라고 생각
def count_char(M, N, board, i, j):

    #탐색시작점 enqueue
    queue = deque([(i,j)])

    #큐가 빌 때까지 반복
    while queue:
        #다음 탐색지점 dequeue
        x, y = queue.popleft()

        #early return (경계값 처리, 1이 아닌 곳)
        if x<0 or x>=M or y<0 or y>=N or board[x][y] == 0:
            continue

        #현재 위치를 그냥 0으로 바꿔줌 (이미 방문한 곳은 다시 볼 필요가 없으므로)
        board[x][y] = 0

        #8방향 정의
        dxy = [(1, 0), (0, 1), (-1, 0), (0, -1),
           (1, 1), (-1, 1), (1, -1), (-1, -1)]

        #8방향 이동
        for dx, dy in dxy:
            queue.append((x+dx, y+dy)) #다음에 탐색할 좌표 enqueue

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

char_cnt = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1: #아직 탐색하지 않은 1의 영역 발견
            char_cnt += 1 #카운트 +1
            count_char(M, N, board, i, j) # BFS 탐색 (이 BFS는 여기서 처음 발견한 1 위치에서 시작해서 이웃한 영역들을 0으로 바꿔 줌)
print(char_cnt)