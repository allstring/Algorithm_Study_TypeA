def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # DP 초기화
    DP = [[[0]*3 for _ in range(N)] for _ in range(N)]
    DP[0][1][0] = 1  # 초기 상태: (1, 1) ~ (1, 2)에 가로로 파이프 배치
    
    # DP 채우기
    for i in range(N):
        for j in range(1, N):
            if board[i][j] == 1:
                continue
            # 가로로 이동
            if j-1 >= 0:
                DP[i][j][0] += DP[i][j-1][0] + DP[i][j-1][1]
            # 세로로 이동
            if i-1 >= 0:
                DP[i][j][2] += DP[i-1][j][1] + DP[i-1][j][2]
            # 대각선으로 이동
            if i-1 >= 0 and j-1 >= 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
                DP[i][j][1] += DP[i-1][j-1][0] + DP[i-1][j-1][1] + DP[i-1][j-1][2]
    
    # 결과 출력
    print(DP[N-1][N-1][0] + DP[N-1][N-1][1] + DP[N-1][N-1][2])

if __name__ == "__main__":
    main()
