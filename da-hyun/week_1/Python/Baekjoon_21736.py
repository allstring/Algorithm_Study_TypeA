dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def main():
    N, M = map(int, input().split())
    friends = [list(input()) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if friends[i][j] == 'I':
                DFS = [(i, j)]
                visited[i][j] = True
                while DFS:
                    x, y = DFS.pop()
                    if(friends[x][y] == 'P'): answer += 1
                    for ddx, ddy in zip(dx, dy):
                        nx, ny = x + ddx, y + ddy
                        if 0 <= nx < N and 0 <= ny < M and friends[nx][ny] != 'X' and not visited[nx][ny]:
                            DFS.append((nx, ny))
                            visited[nx][ny] = True
                if answer: print(answer)
                else: print("TT")
                return
if __name__ == "__main__":
    main()