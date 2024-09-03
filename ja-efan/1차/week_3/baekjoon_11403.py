# 경로 찾기
# Silver I
# https://www.acmicpc.net/problem/11403
"""
풀이 설명 :
    접근 방법 : DFS
    모든 vertex를 순회 하며, 해당 vertex를 root로 하는 깊이 우선 탐색을 진행.
    그래프이기 때문에, 사이클이 존재할 수 있음을 감안해서,
    visited 리스트로 현 경로 상에서 방문 여부를 체크한다.
"""
def dfs(vertex:int, graph:list, visited:list):
    adj_list = graph[vertex]  # 각 vertex에 대한 인접 행렬
    for i in range(len(adj_list)):
        if adj_list[i] == 0 or visited[i]:  # i번째 vertex로의 edge가 없거나, 이미 방문한 경우 continue
            continue
        visited[i] = 1  # 해당 노드를 방문 처리 후 dfs recursion
        dfs(vertex=i, graph=graph, visited=visited)

def main():
    N = int(input())  # 정점의 개수
    graph = [list(map(int, input().split())) for _ in range(N)]  # 그래프 전체에 대한 인접 행렬
    for i in range(N):  # 모든 vertex를 순회하며 깊이 우선 탐색 진행
        visited = [0 for _ in range(N)]  # vertex 별 visited list
        dfs(vertex=i, graph=graph, visited=visited)
        print(*visited)  # 방문 가능한 vertex 출력

if __name__ == "__main__":
    main()