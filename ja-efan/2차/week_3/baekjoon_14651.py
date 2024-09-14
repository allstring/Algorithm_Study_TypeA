# 걷다보니 신천역 삼 (Large)
# Silver I
"""
1 <= N <= 33,333
Time Limit: 2초
    - DFS -> 무조건 터짐
    - DP..? 점화식 유도가 안됨...
    일단 완탐 가보자 -> Do Wa Jo Yo !!


풀이 설명 :
    DFS로 구현 후, N = 10 까지 출력을 확인
    N = i 일 때, 값이 이전 (i-1) 개수의 3배인 것을 확인.
    바로 DP(memoization)으로 구현 완료
"""


def main():
    SAAAAAM = 33333  # 최대 N
    DIVIDOR = 10**9 + 9  # 출력 조건 나누는 수
    N = int(input())

    # DP
    memo = [0 for _ in range(SAAAAAM+1)]  # 최대 N이 들어갈 수 있는 리스트 선언
    memo[2] = 2  # Base case
    for i in range(3, N+1):  # 3 부터 N 까지 순회
        memo[i] = 3 * memo[i-1]  # 점화식
    print(memo[N] % DIVIDOR)  # 출력


if __name__ == "__main__":
    main()