# 이분 그래프
# Gold IV

class DisjointSet:
    def __init__(self, num_v):
        self.head = [0 for _ in range(num_v+1)]
        self.rank = [0 for _ in range(num_v+1)]

    def _make_set(self, v):
        self.head[v] = v

    def make_set_all(self):
        n = len(self.head)
        for v in range(n):
            self._make_set(v)

    def find_head(self, v):
        if self.head[v] != v:
            self.head[v] = self.find_head(self.head[v])
        return self.head[v]

    def union(self, v, u):
        head_of_v = self.head[v]
        head_of_u = self.head[u]
        if head_of_v != head_of_u:
            if self.rank[head_of_v] > self.rank[head_of_u]:
                self.head[head_of_u] = head_of_v
            elif self.rank[head_of_v] < self.rank[head_of_u]:
                self.head[head_of_v] = head_of_u
            else:
                self.head[head_of_v] = head_of_u
                self.rank[head_of_u] += 1


def bipartite_graph():
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    ds = DisjointSet(V)
    ds.make_set_all()
    for v, u in edges:
        ds.union(v, u)

    for i in range(1, V+1):
        ds.find_head(i)
    print(ds.head)
    print(len(set(ds.head)))


def main():
    K = int(input())
    for k in range(K):
        bipartite_graph()


if __name__ == "__main__":
    main()