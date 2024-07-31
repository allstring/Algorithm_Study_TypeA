
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def main():
    T = int(input())

    for test_case in range(T):

        M, N, K = map(int, input().split())
        grid = [[False]*M for _ in range(N)]
        visited = [[False]*M for _ in range(N)]
        for _ in range(K):
            y, x = map(int, input().split())
            grid[x][y] = True
        answer = 0
        for i in range(N):
            for j in range(M):
                if not grid[i][j] or visited[i][j]: continue
                answer += 1
                list = [(i, j)]
                while list:
                    x, y = list.pop(0)
                    # visited[x][y] = True
                    for ddx, ddy in zip(dx, dy):
                        nx, ny = x + ddx, y + ddy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] and not visited[nx][ny]:
                            list.append((nx, ny))
                            #여기가 아니라 위 주석 위치에 visited를 갱신했을 경우 시간초과로 실패
                            #그 이유는?
                            visited[nx][ny] = True

        print(answer)
if __name__ == "__main__":
	main()
