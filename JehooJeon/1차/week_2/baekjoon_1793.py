# 1793. 타일링

import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스가 있는 경우 진행
# 없는 경우 중지
while True:
    try:
        n = int(input())

        # 0 <= n <= 250 범위를 0으로 초기화
        dp = [0] * 251

        # 초기값 설정
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3

        # 점화식을 통해 값을 저장하면서 계산
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] * 2

        print(dp[n])
    except:
        break