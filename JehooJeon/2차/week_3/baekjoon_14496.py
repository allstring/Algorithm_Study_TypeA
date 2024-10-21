from collections import deque, defaultdict
def main():
    def bfs(a, b):
        queue = deque([a])
        visited[a] = 0
        while queue:
            x = queue.popleft()

            if x == b:
                return visited[x]
            for nx in tree[x]:
                if visited[nx] == -1:
                    queue.append(nx)
                    visited[nx] = visited[x] + 1
        return -1

    # a, b: a를 b로 바꾸려하는 문자
    a, b = map(int, input().split())
    # N, M: 전체 문자의 수, 치환 가능한 문자쌍의 수
    N, M = map(int, input().split())
    # tree: 치환 가능한 문자쌍
    tree = defaultdict(list)
    for _ in range(M):
        k, v = map(int, input().split())
        tree[k].append(v)
        tree[v].append(k)
    # visited: 방문 체크 배열 초기화
    visited = [-1] * (N + 1)

    result = bfs(a, b)
    print(result)

if __name__ == "__main__":
    main()