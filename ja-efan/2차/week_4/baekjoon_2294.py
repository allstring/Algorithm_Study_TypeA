# 동전 2
# Gold V

"""
풀이 설명:
    Dynamic Programming
    0원부터 K원까지 i번째 동전을 사용한 최소한의 개수를 저장
"""


def main():
    N, K = map(int, input().split())
    coins = list(set(int(input()) for _ in range(N)))  # 중복 동전 제거 후 리스트 변환
    memo = [K+1 for _ in range(K+1)]

    memo[0] = 0  # 0원을 만드는 데 필요한 동전 개수는 0개

    # 0원 부터 K원까지 메모이제이션
    for k in range(1, K+1):
        # 모든 동전 종류 순회
        for coin in coins:
            # 현재 동전을 사용할 수 있는 경우
            if coin <= k:
                # memo[k]: 이전 동전까지 사용했을 때의 개수
                # memo[k-coin] + 1: 현재 동전을 사용할 수 있도록 공간을 만들어 준 뒤,
                # 현재 동전 사용(+1)
                memo[k] = min(memo[k], memo[k-coin] + 1)

    # K원을 만들 수 있는 경우
    if memo[-1] != K+1:
        print(memo[-1])
        return
    # K 원을 만들지 못한 경우
    print(-1)
    return

if __name__ == "__main__":
    main()