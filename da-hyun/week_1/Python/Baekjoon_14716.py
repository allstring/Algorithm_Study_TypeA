dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0 ,-1, 0, 1 ,-1, 1, -1]

def main():
    N, M = map(int, input().split())
    letters = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and letters[i][j]:
                visited[i][j] = True
                DFS = [(i, j)]
                answer += 1
                while DFS:
                    x, y = DFS.pop()
                    for ddx, ddy in zip(dx, dy):
                        nx, ny = x + ddx, y + ddy
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and letters[nx][ny]:
                            visited[nx][ny] = True
                            DFS.append((nx, ny))

    print(answer)
if __name__ == "__main__":
    main()