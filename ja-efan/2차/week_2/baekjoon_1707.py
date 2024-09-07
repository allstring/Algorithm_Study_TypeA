# 이분 그래프
# Bipartite Graph
# Gold IV
"""
접근법:
    완탐(bfs) 돌면서 하나는 red, 하나는 blue에 넣는다.
    두 노드가 같은 색으로 칠해진 경우: 이분 그래프 형성 불가
"""
from collections import defaultdict, deque

def bipartite():
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    adj_dict = defaultdict(list)
    colors = [0 for _ in range(V+1)]  # 1 or 2
    for v, u in edges:
        adj_dict[v].append(u)
        adj_dict[u].append(v)

    src = 1
    colors[1] = 1
    stack = [src]
    while stack:
        tmp_stack = list()
        while stack:
            curr_vertex = stack.pop()
            curr_color = colors[curr_vertex]
            for adj_vertex in adj_dict[curr_vertex]:
                if not colors[adj_vertex]:
                    colors[adj_vertex] = curr_color % 2 + 1
                    tmp_stack.append(adj_vertex)
                elif colors[adj_vertex] != curr_color:
                    continue
                else:
                    # 인접한 두 정점의 색이 같은 경우
                    # 바로 함수 종료
                    return 'NO'
        stack = tmp_stack
    # print(colors)
    return 'YES'


def main():
    K = int(input())
    for tc in range(1, K+1):
        result = bipartite()
        print(result)

if __name__ == "__main__":
    main()