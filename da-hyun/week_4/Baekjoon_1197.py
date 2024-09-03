# 최소 스패닝 트리(MST)를 구하기 위해 Kruskal 알고리즘을 사용
# Union-Find 알고리즘을 이용하여 사이클을 판별

# Union-Find에서 부모 노드를 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# 두 노드를 하나의 집합으로 합치는 함수
def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def main():
    N = int(input())  # 컴퓨터의 수
    M = int(input())  # 연결할 수 있는 선의 수

    # 간선 리스트 생성
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))  # 비용을 첫 번째 요소로 설정하여 정렬 시 비용을 기준으로 정렬됨

    # 간선을 비용순으로 정렬
    edges.sort()

    # Union-Find 구조를 위한 parent와 rank 배열 초기화
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    # 최소 스패닝 트리를 만들기 위한 변수 초기화
    mst_cost = 0
    edge_count = 0

    # Kruskal 알고리즘으로 최소 스패닝 트리 구성
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):  # 사이클이 생기지 않을 때만 간선 추가
            union(parent, rank, a, b)
            mst_cost += cost
            edge_count += 1
            if edge_count == N - 1:  # N-1개의 간선만 있으면 모든 컴퓨터 연결됨
                break

    # 결과 출력
    print(mst_cost)
if __name__ == "__main__":
    main()