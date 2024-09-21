import sys

input = sys.stdin.readline
mod = 10**9+9 # 나머지 용
n = int(input())
dp = [0] * (4 if n < 4 else n+1)
dp[2] = 2
dp[3] = 6
for i in range(4, n+1):
    dp[i] = dp[i-1] * 3 #이전 값에 3을 곱하는 것이 현재 값
    dp[i] %= mod

print(dp[n])