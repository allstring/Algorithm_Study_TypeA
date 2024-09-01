from collections import deque

def bfs(start, end, graph, n):
    visited = [-1] * (n + 1)  # 방문 체크, -1은 방문하지 않음
    queue = deque([start])  
    visited[start] = 0  # 방문 처리
    
    while queue:
        # print(queue)
        current = queue.popleft()  
        # print(current)
        
        for neighbor in graph[current]:
            if visited[neighbor] == -1: 
                visited[neighbor] = visited[current] + 1  
                queue.append(neighbor)
    
    return visited[end]  

n = int(input()) 
start, end = map(int, input().split())  
m = int(input())  
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