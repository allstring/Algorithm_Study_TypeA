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
        else: # 랭크가 같으면 한 쪽을 루트로 설정하고 랭크++
            parent[rootY] = rootX
            rank[rootX] += 1

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결할 수 있는 간선 수

edges = [] 

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v)) 

# 간선을 가중치 순으로 정렬
edges.sort()

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
mst_cost = 0 # 결과값
count = 0 # 채택 간선 수

for edge in edges:
    w, u, v = edge
    
    # 두 노드가 같은 집합에 속하지 않는 경우에 간선 선택
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        mst_cost += w # 가중치 증가
        count += 1 # 간선 수 ++
    
    # 다 연결했으면 종료
    if count == n - 1:
        break

print(mst_cost)
