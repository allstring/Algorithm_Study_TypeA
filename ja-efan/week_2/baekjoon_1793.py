# 타일링
# Silver II
# https://www.acmicpc.net/problem/1793

"""
풀이 설명 :
    점화식을 세웠다.
    n+2 크기의 직사각형은 n 크기의 직사각형 보다 2x2 만큼의 공간이 더 크기 때문에,
    f(n)에 2x2 직사각형을 채우는 경우의 수를 곱해주면 된다.
    n+1 크기의 직사각형은 n 크기의 직사각형 보다 2x1 만큼의 공간이 더 크기 때문에,
    f(n)에 2x1 직사각형을 채우는 경우의 수를 곱해주면 된다.

    위의 규칙을 n+2 기준으로 바라 보게 되면 f(n) = f(2) x f(n-2) + f(1) x f(n-1)이 된다.
    하지만, 2x2 직사각형을 채우는 경우의 수 중 2x1 타일을 2개 사용 하는 방법은
    f(n-1)에서 2x1 타일을 사용 하는 경우에 포함 된다. (중복은 제거)
    즉, 위에서 정의한 점화식을 base case (f(0) = 1, f(1) = 1, f(2)=3)를 가지는 점화식으로 재정의하면 다음과 같다.
    f(n) = 2 x f(n-2) + f(n-1)
"""
def main():
    while True:  # 테스트 케이스 개수를 정하지 않아 try-except 사용
        try:
            n = int(input())
            if n == 0:
                # 진짜 이거 때문에 몇 번을 시도한건지..
                # 너란 녀석...
                print(1)  # 2 x 0 직사각형이면 공간이 없으니 채우지 않는다. -> 방법 1가지
                continue
            memo = [0 for _ in range(250)]  # 크기를 n으로 주지 않음 <- n 의 범위가 0부터 시작하기 때문
            memo[0] = 1  # base case
            memo[1] = 3  # base case
            for i in range(2, n):
                memo[i] = memo[i - 1] + 2 * memo[i - 2]  # 점화식

            print(memo[n-1])  # 결과 출력

        except :
            break

if __name__ == "__main__":
    main()