import sys
from collections import deque
#input = sys.stdin.readline
def main():
    def calculate_relationship(n, m, relations, a, b):
        tree = {i: [] for i in range(1, n+1)} #가족구성원 1~n, 상하관계 X. 촌수 계산에서 상하관계 중요하지 X
        visited = {i: False for i in range(1, n+1)} #방문여부 표시

        # 트리 구성
        for relation in relations:
            parent, child = relation
            tree[parent].append(child)
            tree[child].append(parent)


        def dfs(node, end, distance): #너비 우선 탐색 알고리즘 이용 - Queue - append, popleft
            visited[node] = True #방문표시
            if node == end: #목표노드 발견
                return distance
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    result = dfs(neighbor, end, distance+1)
                    if result != -1:
                        return result
            return -1

        return dfs(a, b, 0)

    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    relations = [tuple(map(int, input().split())) for _ in range(m)]

    result = calculate_relationship(n, m, relations, a, b)
    print(result)

if __name__ == '__main__':
    main()