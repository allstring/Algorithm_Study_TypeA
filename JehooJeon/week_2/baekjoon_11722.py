# 11722. 가장 긴 감소하는 부분 수열

import sys
sys.stdin = open("input.txt", "r")

# n: 수열의 크기
n = int(input())
# arr: 수열
arr = list(map(int, input().split()))

# dp: 현재 위치 값이 마지막인 감소하는 부분 수열 중 가장 긴 부분 수열 길이
dp = [1] * n

# 만약 위치 값보다 앞 순번에 큰 수가 있으면,
# 그 수에서 +1이 될 수 있음
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
