import heapq

def prim(vertices, edges):
    mst = []

    '''
    adj_list
    딕셔너리
    키 값: 정점
    value: 리스트, (이웃 정점, 가중치)들
    '''
    adj_list = {v:[] for v in vertices}
    for a, b, c in edges:
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))

    visited = set()
    init_vertex = vertices[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]
    #PQ를 가중치값 기준으로 구성해야 하기 때문에 가중치를 맨 앞에 두기
    #min_heap은 priority queue로 사용되며 (가중치, 노드, 인접노드) 순서로 저장됨
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap: #PQ가 빌 때까지 반복
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited: continue

        visited.add(end_v)
        mst.append((start_v, end_v, weight))

        for adj_v, adj_w in adj_list[end_v]: #기준을 end_v로 바꾸어서 탐색
            if adj_v in visited: continue
            heapq.heappush(min_heap, [adj_w, end_v, adj_v])

    return mst

def main():
    N = int(input())
    M = int(input())
    vertices = list(v for v in range(1, N+1))
    edges = [list(map(int, input().split())) for _ in range(M)]
    ans_mst = prim(vertices, edges)
    print(sum(t[2] for t in ans_mst))

if __name__ == '__main__':
    main()