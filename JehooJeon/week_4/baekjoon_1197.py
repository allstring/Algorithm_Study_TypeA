# 1197. 최소 스패닝 트리

import sys
sys.stdin = open('input.txt', 'r')
# 최대 재귀 깊이 변경 -> 런타임 에러 (RecursionError) 해결
sys.setrecursionlimit(10**6)

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        p[py] = px
    else:
        p[px] = py

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())
# edges: 각 간선의 정보(시작정점, 끝정점, 가중치)
edges = [list(map(int, input().split())) for i in range(E)]
# p: 정점 집합
p = [i for i in range(V+1)]

result = 0

edges.sort(key=lambda x: x[2])

for edge in edges:
    if find_set(edge[0]) != find_set(edge[1]):
        union(edge[0], edge[1])
        result += edge[2]

print(result)




''' 메모리 초과
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        p[py] = px
    else:
        p[px] = py

def mst_kruskal(p, edges):
    mst = []

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        s, e, w = edge
        if find_set(s) != find_set(e):
            union(s, e)
            mst.append(edge)
    return mst

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())
# edges: 각 간선의 정보(시작정점, 끝정점, 가중치)
edges = [list(map(int, input().split())) for i in range(E)]
# p: 정점 집합
p = [i for i in range(V+1)]

result = 0
mst = mst_kruskal(p, edges)
for i in mst:
    result += i[2]

print(result)
'''


