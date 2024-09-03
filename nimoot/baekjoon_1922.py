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

n = int(input())  # 컴퓨터의 수
m = int(input())  # 연결할 수 있는 간선의 수

edges = [] 

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v)) 

# 간선을 가중치 순으로 정렬
edges.sort()

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

# 크루스칼 알고리즘
mst_cost = 0 
count = 0 

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

print(mst_cost)
