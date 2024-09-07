import sys
# 이거 없으면 RecurisonError 뜸, 재귀 호출 깊이 제한 늘림
sys.setrecursionlimit(10000)

def dfs(node, distance):
    global max_distance, farthest_node
    visited[node] = True # 방문처리

    if distance > max_distance:
        max_distance = distance
        farthest_node = node
    
    for next_node, weight in tree[node]:
        if not visited[next_node]:
            dfs(next_node, distance + weight)

n = int(input())
if n == 1:  # 노드가 1개면 dfs 돌 필요 없으니까
    print(0)
    exit() # 바로 종료 C++ return 0; 같은 느낌?

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight)) # 부모 노드에 자식 노드 추가
    tree[child].append((parent, weight)) # 자식 노드에 부모 노드 추가

# DFS_1
visited = [False] * (n + 1)
max_distance = 0
farthest_node = 0
dfs(1, 0) # 1번 노드에서 가장 먼 노드를 찾음

# DFS_2
visited = [False] * (n + 1)
max_distance = 0
dfs(farthest_node, 0) # 첫 번째 DFS에서 가장 먼 노드에서 시작

print(max_distance)
