def main():
    N = int(input())
    friends = [list(input()) for i in range(N)]
    to_int = {'N': 0, 'Y': 1}
    friends_matrix = [list(map(lambda x:to_int[x], friend)) for friend in friends]

    dist = [[float('inf')] * N for _ in range(N)]
    for i in range(N): #자기 자신으로의 거리는 0으로 초기화
        dist[i][i] = 0

    for u in range(N): #초기 주어진 가중치에 따라 최초 거리 업데이트(이 문제에서는 두 사람이 직접 친구인 경우)
        for v in range(N):
            if friends_matrix[u][v] == 1:
                dist[u][v] = 1

    #플로이드-워셜 알고리즘 적용
    #모든 정점에 대해 최소 거리 계산
    #경유지 k를 거쳐 가는 것이 더 가깝다면 갱신
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print(max(list(sum(d <= 2 for d in row) for row in dist)) - 1) #자기자신(거리가0)은 제외시켜야 함!


if __name__ == '__main__':
    main()