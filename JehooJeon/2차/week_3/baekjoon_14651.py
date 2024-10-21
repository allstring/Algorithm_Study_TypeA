def main():
    def find_dp(N):
        if N == 1:
            return 0

        dp = [0] * (N + 1)

        dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] * 3

        return dp[N] % 1000000009

    N = int(input())

    result = find_dp(N)
    print(result)

if __name__ == '__main__':
    main()