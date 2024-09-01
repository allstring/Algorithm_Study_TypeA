INF = float('inf')

def floyd_warshall(n, dist):
    # 플로이드-워셜 알고리즘을 이용해서 모든 노드 간 최단 거리 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

dist = [[INF] * n for _ in range(n)]

# 자기 자신은 0, 친구는 1로 설정
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        elif graph[i][j] == 'Y':
            dist[i][j] = 1

floyd_warshall(n, dist)

max_friends = 0

for i in range(n):
    count = 0
    for j in range(n):
        if i != j and dist[i][j] <= 2: 
            count += 1
    max_friends = max(max_friends, count)

print(max_friends)
