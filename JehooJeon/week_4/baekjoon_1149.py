# 1149. RGB거리

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(1):
    # N: 집의 수
    N = int(input())
    # expense: 각 집을 [빨강, 초록, 파랑]으로 칠하는 비용
    expense = [list(map(int, input().split())) for _ in range(N)]

    # 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
    # N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
    # i(2<=i<=N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

    def min_expense(n):
        # 각각의 색을 사용했을 때의 최솟값을 구하기 위한 dp 정의
        dp = [[0, 0, 0] for _ in range(n)]

        # 최초에는 각 값이 최솟값
        dp[0] = expense[0]

        # 이전 집의 색과 같지 않아야 하기 때문에, 현재 값 + 이전 dp의 다른 색 사용 값 중 최솟값 => 최솟값
        for i in range(1, n):
            dp[i][0] = expense[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = expense[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = expense[i][2] + min(dp[i - 1][0], dp[i - 1][1])

        return min(dp[n-1])

    result = min_expense(N)
    print(result)
