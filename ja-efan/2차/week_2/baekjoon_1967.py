# 트리의 지름
# Gold IV

from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

def is_all_visited(vertex:int):
    for adj in adj_dict[vertex]:
        if adj[0] not in visited:
            return False
    return True


def dfs(curr_vertex, acc_weight):
    global MAX_ACC_WEIGHT
    # 탈출 조건?
    # 인접한 노드가 없거나, 인접한 노드가 모두 방문했던 노드인 경우
    if not adj_dict[curr_vertex]:
        MAX_ACC_WEIGHT = max(MAX_ACC_WEIGHT, acc_weight)
        return
    if is_all_visited(curr_vertex):
        MAX_ACC_WEIGHT = max(MAX_ACC_WEIGHT, acc_weight)
        return

    for edge in adj_dict[curr_vertex]:
        if edge[0] in visited: continue
        visited.add(edge[0])
        dfs(edge[0], acc_weight+edge[1])
        visited.remove(edge[0])


def main():
    global visited, adj_dict
    N = int(input())
    adj_dict = defaultdict(list)
    parent = set()
    child = set()
    for _ in range(N-1):
        p, c , w = map(int, input().split())
        adj_dict[p].append((c, w))
        adj_dict[c].append((p, w))
        parent.add(p)
        child.add(c)

    # leaf 중에서 weight 가장 큰 노드를 찾는다
    leaves = set()
    for c in child:
        if c not in parent:
            leaves.add(c)

    max_weight = 0
    max_weight_leaf = None
    for leaf in leaves:
        for edge in adj_dict[leaf]:
            adj_v, w = edge[0], edge[1]
            if max_weight < w:
                max_weight = max(max_weight, w)
                max_weight_leaf = leaf


    visited.add(max_weight_leaf)
    dfs(curr_vertex=max_weight_leaf, acc_weight=0)
    print(MAX_ACC_WEIGHT)


if __name__ == "__main__":
    MAX_ACC_WEIGHT = 0
    adj_dict = None
    visited = set()
    main()