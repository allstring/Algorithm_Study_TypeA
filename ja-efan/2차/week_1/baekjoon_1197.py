# 최소 스패닝 트리
# Gold IV
# MST

"""
풀이 설명:
    서로소 집합(DisjointSet)과 크루스칼 알고리즘을 사용하여 MST를 구성하고,
    MST를 구성하는 edge들의 가중치 합을 계산.
"""


class DisjointSet:
    def __init__(self, num_of_vertices: int):
        self.parent = [0 for _ in range(num_of_vertices + 1)]

    def _make_set(self, v):
        """
        init self.parent[v]

        :param v: vertex
        :return: None
        """
        self.parent[v] = v

    def make_set_all(self, num_of_vertices: int):
        """
        init self.parent

        :param num_of_vertices: number of vertices
        :return: None
        """
        for v in range(num_of_vertices):
            self._make_set(v)

    def find_set(self, v: int) -> int:
        """
        find a representative of v

        :param v: vertex
        :return: representative of v
        """
        if self.parent[v] != v:
            self.parent[v] = self.find_set(self.parent[v])

        return self.parent[v]

    def union(self, v: int, u: int):
        """
        union set of v and set of u

        :param v: vertex
        :param u: vertex
        :return: None
        """
        v_parent = self.parent[v]
        u_parent = self.parent[u]

        if v_parent > u_parent:
            self.parent[v_parent] = u_parent
        else:
            self.parent[u_parent] = v_parent


def kruskal(vertices: list, edges: list):
    """
    make Minimum Spanning Tree using Kruskal algorithm

    :param vertices: list of vertices
    :param edges: list of edges
    :return: weighted sum of edges in MST
    """
    ds = DisjointSet(num_of_vertices=len(vertices))  # 서로소 집합 객체
    ds.make_set_all(len(vertices))  # 각 정점의 대표자 초기화

    # 가중치 기준 정렬 (오름차순)
    edges.sort(key=lambda x: x[2])

    # mst 비용 (간선 가중치들의 합)
    mst_cost = 0

    # 모든 간선을 순회
    for edge in edges:
        v, u, w = edge  # 두 정점과 간선의 가중치
        if ds.find_set(v) != ds.find_set(u):  # 두 정점의 대표자가 같지 않다면
            ds.union(v, u)  # 두 대표자를 합쳐주고,
            mst_cost += w  # mst 비용을 추가

    return mst_cost


def main():
    # V: 정점의 개수 -> [1, 10,000], E: 간선의 개수 -> [1, 100,000]
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    vertices = [v + 1 for v in range(V)]  # 정점 리스트

    mst_cost = kruskal(vertices, edges)

    print(mst_cost)


if __name__ == "__main__":
    main()
