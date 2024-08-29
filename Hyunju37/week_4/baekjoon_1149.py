import sys

def main():
    def find_min(N, cost):
        co = [[0] * 3 for _ in range(N)]
        co[0] = cost[0]
        # 첫 번째 집의 RGB 비용 그대로 초기화

        # i 번쨰 집의 칸 3개에는 각각 해당 집을 그 색깔로 칠했을 때 비용에다가
        # i-1(이전 집)에 칠할 수 있는 2가지 경우의 색 중 더 싼 비용을 더한 값(누적이됨)이 저장됨
        for i in range(1, N):
            for j in range(3):
                co[i][j] = cost[i][j] + min(co[i - 1][(j + 1) % 3], co[i - 1][(j + 2) % 3])

        return min(co[N - 1])


    N = int(sys.stdin.readline())
    cost = []
    for _ in range(N):
        rgb = list(map(int, sys.stdin.readline().split()))
        cost.append(rgb)
    # 각 집마다 RGB 비용 입력받기

    minc = find_min(N, cost)
    print(minc)

if __name__ == '__main__':
    main()