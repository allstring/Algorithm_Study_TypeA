n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))