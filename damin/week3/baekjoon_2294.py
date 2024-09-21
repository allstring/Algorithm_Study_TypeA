import sys

input = sys.stdin.readline
n, k = map(int, input().split()) # 동전 가지수, 목표 가치의 합
coin = [int(input()) for _ in range(n)]
coin_set = set(coin) #동전 중복 방지
coin_list = list(coin_set) # 동전 오름차순 정렬용
coin_list.sort()
dp = [float('INF')] * (k + 1) #동전의 개수가 최소가 되도록 하는 것이므로 최대값을 넣어 초기화
dp[0] = -1
idx = 0 # 제일 작은 동전부터
for i in range(1, k + 1):
    if idx == 0 and i < coin_list[idx]: # 만약 현재 목표 가치의 합(i)이 가지고 있는 동전 중 가장 작은 것보다도 작으면
        dp[i] = -1 # 가지고 있는 동전으로 i를 만들어 낼 수 없으니 -1
    elif i == coin_list[idx]: # 현재 목표가 가지고 있는 동전과 동일하다면
        dp[i] = 1
        if idx < len(coin_list) - 1: # 만약 그 뒤에 동전이 더 있다면 idx 증가
            idx += 1
    else:
        for j in range(idx+1):
            if dp[i - coin_list[j]] != -1: # 동전을 하나 선택한다고 하면 남은 금액이 동전으로 만들 수 있는 금액이어야 함
                dp[i] = min(dp[i], dp[i - coin_list[j]] + 1)
        if dp[i] == float('INF'): # 위에서 가지고 있는 동전으로 모든 경우의 수를 탐색해도 해당 금액을 만들 수 없다면
            dp[i] = -1

print(dp[k])