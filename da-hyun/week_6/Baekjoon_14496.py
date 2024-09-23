def main():
    a, b = map(int, input().split())  # 시작점 a와 목표점 b 입력
    N, M = map(int, input().split())  # 노드 수 N과 간선 수 M 입력
    edges = [set() for _ in range(N+1)]  # 인접 리스트로 그래프 초기화
    visited = [False for _ in range(N+1)]  # 방문 여부 기록

    # 간선 정보 입력
    for _ in range(M):
        x, y = map(int, input().split())
        edges[x].add(y)
        edges[y].add(x)

    # BFS 탐색 초기 설정
    queue = [a]
    visited[a] = True
    day = 0

    while queue:
        tmpQueue = []
        while queue:
            tmpTarget = queue.pop()  # 현재 노드 꺼내기
            if tmpTarget == b:
                print(day)  # 목표점 b에 도달 시 결과 출력
                return
            for neighbor in edges[tmpTarget]:
                if not visited[neighbor]:  # 방문하지 않은 이웃 노드 탐색
                    visited[neighbor] = True
                    tmpQueue.append(neighbor)
        queue = tmpQueue  # 다음 레벨의 노드들로 큐 갱신
        day += 1  # 하루 증가

    # 윗 부분에서 도착했을 때 return을 하라고 했으므로 여기에 도착한다는 건 도착하지 못한 경우라는 뜻
    print(-1)  # 목표점 b에 도달하지 못한 경우 -1 출력
if __name__ == '__main__':
    main()
