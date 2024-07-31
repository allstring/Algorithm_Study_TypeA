dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def main():
    N, M, K = map(int, input().split())
    grid = [[False]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        grid[x-1][y-1] = True
    answer = 0
    for i in range(N):
        for j in range(M):
            if not grid[i][j] or visited[i][j]: continue
            DFS = [(i, j)]
            tmpAnswer = 1
            visited[i][j] = True
            while DFS:
                x, y = DFS.pop()
                for ddx, ddy in zip(dx, dy):
                    nx, ny = x+ddx, y+ddy
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] and not visited[nx][ny]:
                        DFS.append((nx, ny))
                        visited[nx][ny] = True
                        tmpAnswer += 1
            answer = max(tmpAnswer, answer)
    print(answer)
if __name__ == "__main__":
    main()