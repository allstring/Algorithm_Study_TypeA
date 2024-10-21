# 1922. 네트워크 연결

import sys
sys.stdin = open('input.txt', 'r')

# N: 컴퓨터의 수(정점의 수)
N = int(input())
# M: 연결할 수 있는 선의 수(간선의 수)
M = int(input())
# edges: 비용의 정보(시작, 끝, 비용)
edges = [list(map(int, input().split())) for _ in range(M)]
# vertices: 정점 집합
vertices = [i for i in range(N+1)]

def find_set(x):
    if x != vertices[x]:
        vertices[x] = find_set(vertices[x])
    return vertices[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        vertices[py] = px
    else:
        vertices[px] = py

def mst_kruskal(vertices, edges):
    # MST 저장
    mst = []
    # 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        # s, e, w: 시작정점, 도착정점, 가중치(비용)
        s, e, w = edge
        # 만약 시작정점이 도착정점과 다른 집합에 속한 경우
        if find_set(s) != find_set(e):
            # 시작정점과 도착정점의 집합을 합침
            union(s, e)
            # 현재 간선을 MST에 추가
            mst.append(edge)
    return mst


result = 0
mst = mst_kruskal(vertices, edges)
# MST의 가중치(비용)을 모두 더해줌
for i in mst:
    result += i[2]

print(result)
