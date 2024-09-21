from collections import defaultdict
import sys
'''
가장 먼 트리의 지름을 구할 때 완전 탐색 -> 시간 초과
따라서 제일 먼 곳을 구한 후 그곳에서 다시 먼 곳을 구하기
'''
sys.setrecursionlimit(100000) # 재귀 깊이 제한 늘리기

def dfs(node, weight):
    global max_distance, farthest_node
    visited[node] = True

    if weight > max_distance: #지금까지의 거리가 최대 거리를 넘으면
        max_distance = weight
        farthest_node = node

    for neighbor in tree_structure[node]: #방문 안한 노드 탐색
        if not visited[neighbor]:
            dfs(neighbor, weight + tree_structure[node][neighbor])

    visited[node] = False

n = int(input())
tree_structure = defaultdict(dict)

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree_structure[parent][child] = weight
    tree_structure[child][parent] = weight  # 트리는 양방향 그래프이므로 양쪽에 다 추가


visited = [False] * (n + 1) #방문 여부 저장
max_distance = 0
farthest_node = 1
dfs(1, 0) # 가장 먼 노드 찾기

max_distance = 0 #초기화
dfs(farthest_node, 0) #가장 먼 노드에서부터 가장 먼 노드 찾기

print(max_distance)
