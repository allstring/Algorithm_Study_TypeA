def main():
    def create_cannon(N):
        dp = [0, 1]

        if N == 1:
            return dp

        idx = 2
        while True:
            next_dp = dp[idx - 1] + (idx * (idx + 1)) // 2
            # 만약, 다음 값이 N보다 클 경우에는 return
            if next_dp > N:
                return dp

            # 다음 값이 N보다 크지 않을 경우에는 dp에 추가하고 idx 1 추가
            dp.append(next_dp)
            idx += 1

    def find_dp(N, arr):
        dp = [float("inf")] * (N + 1)

        for i in range(1, N + 1):
            for num in arr:
                # i 값과 같은 값이 있을 경우에는 1
                if num == i:
                    dp[i] = 1
                    break
                # 갯수가 더 많은 경우 패스
                elif num > i:
                    break
                # 만약, 요소 값이 더 작을 경우에는 이전 dp와 비교해서 작은 값
                dp[i] = min(dp[i], 1 + dp[i - num])

        return dp[N]

    N = int(input())

    cannon_balls = create_cannon(N)
    result = find_dp(N, cannon_balls)
    print(result)

if __name__ == '__main__':
    main()

