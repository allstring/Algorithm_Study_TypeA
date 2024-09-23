def main():
    N = int(input())
    dp = [0] * (N + 1)
    if N == 1:
        print(0)
        return
    elif N == 2:
        print(2)
        return
    dp[1] = 0 #초기 값 N=1 초기화
    dp[2] = 2 #초기 값 N=2 초기화
    #다음과 같은 점화식이 가능한 이유
    #(0,1,2) % 3 = (0,1,2)
    #이미 정해진 앞자리 숫자들 + 추가 한 자리 _
    #가 3k가 되는 경우 _에는 한 가지 경우의 수밖에 없음.
    for i in range(3, N+1):
        dp[i] = dp[i-1] * 3
    print(dp[N]%1000000009)

if __name__ == "__main__":
    main()