import sys
from collections import deque

def get_binary_graph(K, V, edges):
    # 그래프 초기화
    graph = [[] for _ in range(K + 1)]
    
    # 간선 입력 받아 그래프 구성
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 방문 상태 (-1: 방문 안 함, 0: Red, 1: Blue)
    visited = [-1 for _ in range(K + 1)]
    
    # 각 정점에 대해 BFS 탐색 수행
    for k in range(1, K + 1):
        if visited[k] == -1:
            queue = deque([k])
            visited[k] = 0  # 첫 번째 정점은 Red로 방문
            
            # BFS 탐색
            while queue:
                node = queue.popleft()
                current_color = visited[node]
                
                # 인접한 정점 방문
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:  # 아직 방문하지 않은 경우
                        visited[neighbor] = 1 - current_color  # 다른 색으로 방문
                        queue.append(neighbor)
                    elif visited[neighbor] == current_color:  # 같은 색으로 방문되면 이분 그래프가 아님
                        return False
    # 모든 정점 탐색 후 이분 그래프 판별 성공
    return True

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        K, V = int(data[idx]), int(data[idx+1])
        idx += 2
        edges = []
        for _ in range(V):
            u, v = int(data[idx]), int(data[idx+1])
            edges.append((u, v))
            idx += 2
        
        if get_binary_graph(K, V, edges):
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    main()
