## 다른 문제로 착각해서 푼 풀이인데
## n개 종류의 동전들로 k원을 만들 수 있는 경우의 수 구하기

# def main():
#     n, k = map(int, input().split())
#     coins = [int(input()) for _ in range(n)]
#     DP = [0 for _ in range(k+1)]
#     for coin in coins:
#         tmpDP = [0 for _ in range(k+1)]
#         tmpDP[0] = 1
#         for i in range(1,k+1):
#             tmpDP[i] += DP[i]
#             if i >=coin: tmpDP[i] += tmpDP[i-coin]
#         DP = tmpDP
#     print(DP[k])
# if __name__ == "__main__":
#     main()


def main():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]  # 동전 리스트 입력

    # DP 배열 초기화, 무한대로 설정 (K+1 크기)
    DP = [float('inf') for _ in range(K+1)]
    coins.sort()  # 동전 리스트 정렬

    # DP[i] = i원을 만들 수 있는 최소 동전의 개수
    # 1660번 문제랑 상당 부분 동일함
    # DP를 통해 최소 동전 수 계산
    for i in range(1, K+1):
        for coin in coins:
            if i == coin:  # 한개의 동전으로 만들 수 있을 때
                DP[i] = 1
            elif coin > i:  # 동전 모두 탐색하면 종료
                break
            else:  # DP를 갱신해 최소값 계산
                DP[i] = min(DP[i], DP[i-coin] + 1)

    # 목표 값 K에 해당하는 최소 동전 수 출력, 불가능하면 -1 출력
    print(DP[K] if DP[K] != float('inf') else -1)
if __name__ == "__main__":
    main()
