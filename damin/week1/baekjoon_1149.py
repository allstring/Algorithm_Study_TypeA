'''
서로 다른 색으로 집을 색칠해야 한다면 n번째 집의 색을 고정한 후 생각
n번째 집이 빨강일 경우 n-1번째 집은 초록 아니면 파란색
n-1번째 집을 칠할 때 까지의 최소값(초록, 파랑 중 최소값 선택) + n번째 집 칠하는 비용 
=> n번째 집 칠하는 최소 비용
'''

import sys

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[1] = cost[0]

for i in range(2, n+1):
    #맨 마지막 집이 빨간색으로 칠한다고 했을 때 그 전 집은 초록 or 파랑인데 그 중에서 최소값 구하기
    dp[i][0] = cost[i-1][0] + min(dp[i-1][1], dp[i-1][2]) 
    dp[i][1] = cost[i-1][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i-1][2] + min(dp[i-1][1], dp[i-1][0])
print(min(dp[n]))