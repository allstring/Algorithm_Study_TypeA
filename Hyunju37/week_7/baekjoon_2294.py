def main():
    n, k = list(map(int, input().split()))
    coins = [int(input()) for _ in range(n)]

    #dp 배열 초기화
    dp = [0] * (k+1)
    dp[0] = 1

    #1부터 k까지 반복
    for i in range(1, k+1):
        # 그 값 단위동전이 있으면 해당 동전 한 개로 값 채울 수 있음
        if i in coins:
            dp[i] = 1
            continue
        #i보다 작은 단위동전들 목록
        smaller_coins = [c for c in coins if c <= i]
        #i보다 작은 단위동전들이 없다면 해당 값을 채울 수 없음, 0
        if len(smaller_coins) == 0:
            dp[i] = 0
            continue
        try:
            #s원짜리 동전을 쓰는 방법들 고려하기
            ways = [dp[i-s]+1 for s in smaller_coins if dp[i-s] > 0]
            #동전을 최소 개수로 쓰는 방법
            min_way = min(ways)
        #만약 고려 가능한 방법들이 없다면 empty list에서 min을 계산하려고 하니까
        #오류발생 -> catch
        except Exception:
            dp[i] = 0
            continue
        dp[i] = min_way

    if dp[k]:
        print(dp[k])
    else:
        print(-1)

if __name__ == "__main__":
    main()