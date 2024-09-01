# 유니온 파인드(Disjoint Set) 자료구조
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

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

# 입력 처리
n = int(input())  # 컴퓨터의 수 (노드 수)
m = int(input())  # 연결할 수 있는 간선의 수

edges = []  # 간선 정보를 저장할 리스트

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))  # 가중치, 시작 노드, 끝 노드 순으로 저장

# 간선을 가중치 순으로 정렬
edges.sort()

# 유니온 파인드 초기화
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

# 크루스칼 알고리즘 수행
mst_cost = 0  # 최소 스패닝 트리의 비용
count = 0  # 선택한 간선의 개수

for edge in edges:
    w, u, v = edge
    
    # 두 노드가 같은 집합에 속하지 않는 경우에만 선택
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        mst_cost += w
        count += 1
    
    # 모든 노드를 연결했으면 종료
    if count == n - 1:
        break

# 결과 출력
print(mst_cost)
