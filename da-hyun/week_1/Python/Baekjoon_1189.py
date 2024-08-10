dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def recursive(x, y, depth, board, visited, R, C, K):
    # print((x, y))
    visited[x][y] = True
    if(x, y) == (0, C-1) or depth == K:
        visited[x][y] = False
        if((x,y) == (0,C-1) and depth == K): return 1
        return 0
    tmpAnswer = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if(0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny]):
            tmpAnswer += recursive(nx, ny, depth + 1, board, visited, R, C, K)
    visited[x][y] = False
    return tmpAnswer

def main():
    R, C, K = map(int, input().split())
    board = [list(map(lambda x: x=='.', input())) for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    print(recursive(R-1, 0, 1, board, visited, R, C, K))

if __name__ == "__main__":
    main()