# 14712. 넴모넴모

# import sys
# sys.stdin = open('baekjoon_14712_input.txt', 'r')

def dfs(board, cnt):
    global result
    # 모든 칸을 모두 탐색한 경우
    if cnt == N * M:
        result += 1
        return
    
    x = cnt // M + 1
    y = cnt % M + 1

    # 넴모를 놓을 수 있는 경우
    if board[x - 1][y] == 0 or board[x - 1][y - 1] == 0 or board[x][y - 1] == 0:
        board[x][y] = 1
        dfs(board, cnt + 1)
        board[x][y] = 0    # 다시 복구
    # 넴모를 놓을 수 없는 경우
    dfs(board, cnt + 1)

def main():
    global N, M, result
    # N, M: 격자판의 행의 개수, 열의 개수
    N, M = map(int, input().split())
    # nemmo: 넴모넴모 격자판
    nemmo = [[0] * (M + 1) for _ in range(N + 1)]
    result = 0

    dfs(nemmo, 0)
    print(result)

if __name__ == '__main__':
    main()