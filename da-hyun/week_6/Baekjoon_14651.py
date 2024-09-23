def main():
    N = int(input())  # 입력 값 N
    # N이 2 이상일 때 식을 계산하여 출력, 그렇지 않으면 0 출력
    # 경우의 수 가지를 그려보면 쉬움..
    print(2 * (3 ** (N - 2)) % (10**9 + 9) if N >= 2 else 0)
if __name__ == '__main__':
    main()
