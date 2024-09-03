# 네트워크 연결
# Gold IV

"""
풀이 설명 :
    서로소 집합과 크루스칼 알고리즘을 이용하여 MST를 구성.
    전체 컴퓨터를 연결하는 최소 비용의 네트워크를 구성.
"""

# DisjointSet 클래스
class DisjointSet:
    def __init__(self, n_vertices):
        self.parents = [0 for _ in range(n_vertices+1)]

    def make_set(self, x):
        self.parents[x] = x

    def find_set(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find_set(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px > py:
            self.parents[px] = py
        else:
            self.parents[py] = px

    def get_parents(self):
        return self.parents


def main():
    N = int(input())  # 컴퓨터의 수
    M = int(input())  # 연결 가능한 선의 수

    edges = [tuple(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])  # 가중치 기준 정렬
    ds = DisjointSet(N)  # disjoint-set 객체

    # 대표자(parent) 초기화
    for computer in range(1, N+1):
        ds.make_set(computer)

    cost = 0  # mst 비용
    # mst_edges = []
    # kruskal algorithm
    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):  # 두 컴퓨터의 대표자가 같지 않으면 union
            ds.union(s, e)
            cost += w
            # mst_edges.append(edge)
    # print(mst_edges)
    print(cost)


if __name__ == "__main__":
    main()