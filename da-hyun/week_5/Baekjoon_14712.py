def can_place(prev_row, curr_row, m):
    # 2x2 사각형이 형성되는지 체크
    for j in range(m - 1):
        # 현재 칸과 오른쪽 칸, 윗줄 두 칸이 모두 넴모인 경우 2x2 사각형이 형성됨
        if (prev_row & (1 << j)) and (prev_row & (1 << (j + 1))) and (curr_row & (1 << j)) and (curr_row & (1 << (j + 1))):
            return False  # 2x2 사각형이 형성되므로 이 상태는 유효하지 않음
    return True  # 2x2 사각형이 형성되지 않으면 유효한 상태

def nemo_game(N, M):
    # dp 배열을 생성합니다. 행 개수 N+1, 열 상태 1<<M 크기
    dp = [[0] * (1 << M) for _ in range(N + 1)]
    dp[0][0] = 1  # 초기 상태: 첫 번째 행이 비어있는 상태
    
    for i in range(1, N + 1):  # 첫 번째 행부터 N번째 행까지 처리
        for prev_row in range(1 << M):  # 이전 행의 모든 상태(2^M 가지)
            if dp[i-1][prev_row] > 0:  # 이전 행이 유효한 상태일 때만
                for curr_row in range(1 << M):  # 현재 행의 모든 상태(2^M 가지)
                    if can_place(prev_row, curr_row, M):  # 2x2 사각형이 만들어지지 않는 경우만
                        dp[i][curr_row] += dp[i-1][prev_row]  # 상태 전이: 가능한 경우의 수를 더함

    # 마지막 행까지 고려했을 때 모든 유효한 배치의 수를 합산해서 반환
    return sum(dp[N])

# 입력
N, M = map(int, input().split())  # N: 행의 수, M: 열의 수
# 결과 출력
print(nemo_game(N, M))
