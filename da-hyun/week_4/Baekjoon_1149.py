def main():
    N = int(input())
    # 입력 받기
    map = [[int(input()) for _ in range(N)] for _ in range(3)]
    # 현재 최소 값 저장. temp_minimum은 갱신할 장소, minimum은 이전 최소 값을 저장해 둘 장소.
    temp_minimum = [map[0][0], map[1][0], map[2][0]]
    minimum = temp_minimum[:]

    for i in range(1, N):
        # temp_minimum[i][j] : i번 인덱스에 j 색을 칠했을 때 최소값.
        # temp_minimum[i][j] = min(temp_minimum[i][k], temp_minimum[i][l]) + map[i][j] (단 j,k,l은 모두 다른 숫자)
        temp_minimum = [min(minimum[(j+1)%3], minimum[(j+2)%3]) + map[j][i] for j in range(3)]
        minimum = temp_minimum[:]

    print(min(minimum))

if __name__ == "__main__":
    main()
