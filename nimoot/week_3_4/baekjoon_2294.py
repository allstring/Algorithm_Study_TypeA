'''
1660이랑 비슷함
1660은 사면체 배열 만들어야 했는데, 이거는 배열이 입력으로 받아지는 거고,
로직은 똑같음
'''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp=[float('inf')] * (k + 1)
dp[0] = 0 

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] != float('inf'):
    print(dp[k])
else:
    print(-1)