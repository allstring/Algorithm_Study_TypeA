from collections import deque

def bfs(start, end, graph, n):
    visited = [-1] * (n + 1)  # 방문 체크, -1은 방문하지 않음
    queue = deque([start])  
    visited[start] = 0  # 방문 처리
    
    while queue:
        current = queue.popleft()  
        
        for neighbor in graph[current]:
            if visited[neighbor] == -1: # 아직 방문 안했으면
                visited[neighbor] = visited[current] + 1  # 현재 노드까지 거리 ++해서 이웃 노드 거리 설정
                queue.append(neighbor)
    
    # 목표 노드 거리 반환
    return visited[end]  

n = int(input()) # 사람(노드)
start, end = map(int, input().split())  
m = int(input()) # 관계(간선)
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# print(start)
# print(end)
result = bfs(start, end, graph, n)

print(result)