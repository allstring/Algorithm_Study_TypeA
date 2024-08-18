# 플로이드-워셜 알고리즘을 사용하여 모든 노드 간의 경로를 계산하는 함수
def floyd_warshall(graph):
    n = len(graph)  # 그래프의 노드 수
    for k in range(n):  # 경유 노드 k
        for i in range(n):  # 시작 노드 i
            for j in range(n):  # 도착 노드 j
                # 경유 노드를 거쳐서 갈 수 있는 경로가 있으면 1로 설정
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    return graph

def main():
    n = int(input())  # 그래프의 크기 입력
    graph = [list(map(int, input().split())) for _ in range(n)]  # 그래프 입력

    # 플로이드-워셜 알고리즘 결과 출력
    for row in floyd_warshall(graph):
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
