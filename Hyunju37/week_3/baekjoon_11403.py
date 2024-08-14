

def main():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    reachable = [[0] * N for _ in range(N)]
    for start in range(N): #정점 0부터 정점 N-1까지 출발점으로 지정
        #visited = [False] * N
        stack = [start]
        while stack:
            node = stack.pop()
            for adj_node, adj in enumerate(graph[node]):
                if adj == 1:
                    if not reachable[start][adj_node]:
                        stack.append(adj_node)
                        #visited[adj_node] = True
                        reachable[start][adj_node] = 1

    for i in range(N):
        for j in range(N):
            print(reachable[i][j], end = ' ')
        print()

if  __name__ == '__main__':
    main()