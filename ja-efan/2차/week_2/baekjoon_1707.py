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
    adj_dict = defaultdict(list)  # 인접 리스트
    colors = [0 for _ in range(V+1)]  # 각 정점에 칠한 색을 표시(방문 여부도 체크) : 1 or 2
    # 인접 리스트 구성 (defaultdict)
    for v, u in edges:
        adj_dict[v].append(u)
        adj_dict[u].append(v)

    # 모든 정점을 순회 (그래프 문제 이므로, 모든 정점이 이어져 있을 거라 생각 x)
    for src_vertex in range(1, V+1):
        if colors[src_vertex]: continue  # 이미 방문한(색 칠한) 정점의 경우 skip
        colors[1] = 1  # 시작 정점 1로 색칠
        stack = [src_vertex]
        while stack:
            tmp_stack = list()  # 임시 스택
            while stack:
                curr_vertex = stack.pop()  # 정점 하나 pop
                curr_color = colors[curr_vertex]  # 현재 정점의 색
                for adj_vertex in adj_dict[curr_vertex]:  # 현재 정점과 인접한 정점 순회
                    if not colors[adj_vertex]:  # 방문하지 않은(색이 없는) 정점
                        colors[adj_vertex] = curr_color % 2 + 1  # 현재 정점과 다른 색으로 색칠
                        tmp_stack.append(adj_vertex)  # 임시 스택에 저장
                    elif colors[adj_vertex] != curr_color:  # 방문한 정점이지만, 현재 정점과 다른 색인 경우 스킵
                        continue
                    else:
                        # 인접한 두 정점의 색이 같은 경우
                        # 바로 함수 종료
                        return 'NO'
            stack = tmp_stack  # 임시 스택을 메인 스택으로 변경
    return 'YES'  # 주어진 그래프가 '이분 그래프'인 경우


def main():
    K = int(input())
    for tc in range(1, K+1):
        result = bipartite()
        print(result)

if __name__ == "__main__":
    main()