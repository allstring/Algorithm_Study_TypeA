from collections import defaultdict
import sys

sys.setrecursionlimit(10000)

"""
트리의 지름:
    1. 임의의 정점에서 가장 먼 정점 A를 찾는다. 
        -> from ROOT to A
    2. 정점 A에서 가장 먼 정점 B를 찾는다.
        -> from A to B  
    => 정점 A에서 B로의 경로가 트리의 지름이다.
"""


def is_all_visited(vertex):
    # 현재 정점에 인접한 정점들의 방문 여부를 확인한다.
    # 모두 방문한 경우 True
    # 하나라도 방문하지 않은 경우 False
    adj_list = edges[vertex]
    for adj_vertex, _ in adj_list:
        if adj_vertex not in visited:
            return False
    return True


def dfs(current_vertex, acc_weight, ):
    global diameter, vertex_A, visited
    # 탈출 조건:
    # 인접한 정점이 없거나,
    if not edges[current_vertex]:
        if diameter < acc_weight:
            diameter = acc_weight
            # print(f"paths: {paths}, diameter: {diameter}")
            vertex_A = current_vertex
            return
    # 인접한 정점을 모두 방문한 경우
    if is_all_visited(vertex=current_vertex):
        if diameter < acc_weight:
            diameter = acc_weight
            # print(f"paths: {paths}, diameter: {diameter}")
            vertex_A = current_vertex
            return

    # # 현재 정점을 방문 처리
    # visited.add(current_vertex)

    # 인접한 정점에 대하여 백트래킹
    adj_list = edges[current_vertex]
    for adj_vertex, weight in adj_list:
        if adj_vertex in visited:
            continue
        # 인접 정점 방문 처리
        visited.add(adj_vertex)
        # dfs
        dfs(current_vertex=adj_vertex, acc_weight=acc_weight + weight)
        # 방문 처리 원복
        visited.remove(adj_vertex)


# 1. 루트(1)에서 가장 먼 노드를 찾는다.
# -> 내려갈 때마다 weight를 누적해준다.

def main():
    global edges, visited

    N = int(input())
    edges = defaultdict(list)
    # weights_from_root = defaultdict(int)
    # weights_from_root[1] = 0
    for _ in range(N - 1):
        p, c, w = map(int, input().split())
        # edges.append((p, c, w))
        edges[p].append((c, w))
        # weights_from_root[c] = weights_from_root[p] + w
        edges[c].append((p, w))

    # print(edges)

    # weights_from_root = list(sorted(weights_from_root.items(), key=lambda x: x[1], reverse=True))
    # print(weights_from_root)


    # 루트(1)에서 가장 먼 노드 A
    # vertex_A = weights_from_root[0][0]
    visited.add(1)
    dfs(current_vertex=1, acc_weight=0)
    # print(vertex_A)
    visited.remove(1)
    ####################################################
    visited.add(vertex_A)
    init_weight = 0
    dfs(current_vertex=vertex_A, acc_weight=init_weight)

    print(diameter)


if __name__ == "__main__":
    # 글로벌 변수 선언
    edges = None
    visited = set()
    diameter = 0  # 트리의 지름
    vertex_A = None

    main()