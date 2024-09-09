# 방향 벡터 설정: 상, 우, 하, 좌 (순서대로)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def main():
    # 입력받아 M(열), N(행) 저장
    M, N = map(int, input().split())
    
    # 그리드 입력받기
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    queue = []  # BFS를 위한 큐 초기화
    allCount = M * N  # 전체 칸 수
    
    # 초기 상태에서 익은 토마토 위치 파악 및 전체 칸 수에서 -1 위치 제외
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j))  # 익은 토마토 위치 저장
            elif grid[i][j] == -1:
                allCount -= 1  # 빈 칸 제외
    
    days = -1  # 날짜 초기화
    
    # BFS 탐색 시작
    while queue:
        allCount -= len(queue)  # 현재 큐에 있는 칸 수만큼 전체 칸 수에서 제외
        days += 1  # 하루 증가
        
        # 다음 단계에서의 큐를 저장할 임시 큐
        tmpQueue = []
        
        # 현재 큐에 있는 모든 위치 탐색
        while queue:
            x, y = queue.pop()  # 큐에서 위치를 꺼내기
            # 4방향으로 인접한 위치 탐색
            for ddx, ddy in zip(dx, dy):
                nx, ny = x + ddx, y + ddy
                # 유효한 범위 내에 있고, 익지 않은 토마토가 있는 경우
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                    tmpQueue.append((nx, ny))  # 임시 큐에 추가
                    grid[nx][ny] = 1  # 해당 위치 토마토를 익은 상태로 변경
        
        queue = tmpQueue  # 현재 큐를 다음 단계 큐로 교체
    
    # 모든 토마토가 익지 못한 경우
    if allCount:
        print(-1)
    # 모든 토마토가 익은 경우
    else:
        print(days)

if __name__ == "__main__":
    main()
