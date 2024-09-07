# 1967. 트리의 지름

import sys
sys.stdin = open('baekjoon_1967_input.txt', 'r')

import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

def main():
    def dfs(start, weight):
        # 도착 노드와 가중치를 저장
        for n, n_d in tree[start]:
            # 만약 distance를 계산하지 않았다면,
            # 시작 노드를 기준으로 도착 노드들의 가중치 더해줌
            if distance[n] == -1:
                distance[n] = weight + n_d
                dfs(n, weight + n_d)
        return

    # n: 노드의 개수
    n = int(input())
    # tree: 각 노드에 대한 정보
    tree = defaultdict(list)
    for _ in range(n-1):
        p, c, w = map(int, input().split())
        tree[p].append((c, w))
        tree[c].append((p, w))

    # distance: 시작 정점에서 임의의 정점까지의 거리를 측정
    distance = [-1] * (n + 1)
    distance[1] = 0
    dfs(1, 0)

    start = distance.index(max(distance))
    distance = [-1] * (n + 1)
    distance[start] = 0
    dfs(start, 0)

    print(max(distance))
    
if __name__ == '__main__':
    main()