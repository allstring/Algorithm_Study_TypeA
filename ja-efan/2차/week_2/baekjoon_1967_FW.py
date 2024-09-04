# 트리의 지름
# Gold IV

def floyd_warshall():
    N = int(input())  # 노드의 개수
    distances = [[INF for _ in range(N)] for _ in range(N)]
    for _ in range(N-1):
        p, c, w = map(int, input().split())
        distances[p-1][c-1] = w
        distances[c-1][p-1] = w

    for k in range(N):
        distances[k][k] = 0
        for i in range(N):
            if k == i: continue
            for j in range(N):
                if k == j or i == j: continue
                distances[i][j] = min(distances[i][k] + distances[k][j], distances[i][j])

    print(max([max(row) for row in distances]))


if __name__ == "__main__":
    INF = float('inf')
    floyd_warshall()



