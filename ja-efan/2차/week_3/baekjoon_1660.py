# 캡틴 이다솜
# Silver I

def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    k_prime_list = [0 for _ in range(N+1)]
    k_prime_list[1] = 1
    k_prime_list[2] = 4
    for k in range(3, N+1):
        k_prime_list[k] = int(k_prime_list[k-1] + (k*(k+1)) / 2)

    print(k_prime_list)

    # memoization 배열 초기화
    memo = [[0 for _ in range(N+1)]]
    k = 1
    while k_prime_list[k] < N:
        if k == 1:
            memo.append([i for i in range(N+1)])
        else:
            memo.append([0 for _ in range(N+1)])
        k += 1
        # if k_prime_list[k+1] == N:
        #     memo.append([0 for _ in range(N+1)])
    # memo.append([0 for _ in range(N+1)])
    print(f"shape: {len(memo), len(memo[0])}")

    for k in range(1, len(memo)):
        k_prime = k_prime_list[k]
        print(k_prime)
        for n in range(1, N+1):
            # print(k, n)
            if N < k_prime:
                memo[k][n] = memo[k-1][n]
            elif N == k_prime:
                memo[k][n] = 1
            elif N > k_prime:
                memo[k][n] = (n // k_prime) + (memo[k-1][n % k_prime])
        print(memo)
    # print(memo)
    print(memo[-1][N])
    return

if __name__ == "__main__":
    main()