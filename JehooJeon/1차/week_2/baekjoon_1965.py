# 1965. 상자넣기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))

    # 최초에 dp 리스트를 1로 초기화
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # 이전 값 중에서 현재 값보다 작은 값이 있다면, 
            # 이전 값에서의 dp 값과 현재 값의 dp 값 중 큰 값으로 설정
            if num_list[i] > num_list[j]:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))