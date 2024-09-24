def main():
    N = int(input())  # 입력 값 N
    tetrahedrons = []  # 정사면체 저장
    sum, index = 1, 2
    while sum <= N:
        tetrahedrons.append(sum)  # 테트라헤드론 값 저장
        sum += (index * (index + 1)) // 2  # 다음 테트라헤드론 계산
        index += 1  # 인덱스 증가

    # DP 배열 초기화, 무한대로 설정 (N+1인 이유는 indexing 때문)
    DP = [float('inf') for _ in range(N+1)]

    # DP[i] = i개로 만들 수 있는 정사면체 최소 갯수.
    # DP를 통해 최소 테트라헤드론 수 계산
    for i in range(1, N+1):
        for tetra in tetrahedrons:
            if i == tetra: # 한개의 정사면체를 만들 수 있을 때
                DP[i] = 1
            elif tetra >= i:  # 가능한 정사면체를 모두 탐색했을 때 종료.
                break
            else:  # DP를 갱신해 최소값 계산
                DP[i] = min(DP[i], DP[i-tetra] + 1)

    print(DP[N])  # 결과 출력
if __name__ == "__main__":
    main()
