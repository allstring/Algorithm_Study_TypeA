# 21937. 작업


import sys
sys.stdin = open("input.txt", "r")

def dfs(current, visited):
    global count

    # 현재 위치 방문 표시
    visited[current] = True

    for idx, value in enumerate(work_seq):
        if visited[idx]:
            continue
        if current in value:
            count += 1
            dfs(idx, visited)

T = int(input())

for _ in range(T):
    # n: 작업할 개수, m: 작업 순서 정보의 개수
    n, m = map(int, input().split())
    # work_seq: 작업 선후 관계 리스트
    work_seq = [[] for _ in range(n)]
    for _ in range(m):
        i, j = map(int, input().split())
        work_seq[i - 1].append(j - 1)
    # visited: 방문 체크
    visited = [False] * n
    # x: 반드시 끝내야 하는 작업
    x = int(input()) - 1

    # print(n, m)
    # print(work_seq)
    # print(x)
    # print(visited)

    count = 0
    dfs(x, visited)
    print(count)



    ''' 런타임 에러
    # n: 작업할 개수, m: 작업 순서 정보의 개수
    n, m = map(int, input().split())
    # work_matrix: 인접작업 배열
    work_matrix = [[0] * n for _ in range(n)]
    for _ in range(m):
        i, j = map(int, input().split())
        # 인덱스는 0부터 시작하므로 -1
        work_matrix[i - 1][j - 1] = 1
    # 방문체크 배열
    visited = [False] * n
    # x: 오늘 반드시 끝내야하는 작업 -> 인덱스는 0부터 시작하므로 -1
    x = int(input()) - 1

    # print(work_matrix)
    # print(visited)
    # print(x)

    count = 0

    def dfs(current, work_matrix, visited):
        global count
        # 방문한 지점 표시
        visited[current] = True

        for i in range(len(work_matrix)):
            if work_matrix[i][current] and not visited[i]:
                count += 1
                dfs(i, work_matrix, visited)


    dfs(x, work_matrix, visited)
    print(count)
    '''



    ''' 메모리 초과
    # n: 작업할 개수, m: 작업 순서 정보의 개수
    n, m = map(int, input().split())
    # work_matrix: 인접작업 배열
    work_matrix = [[] for _ in range(n)]
    for _ in range(m):
        i, j = map(int, input().split())
        # 인덱스는 0부터 시작하므로 -1
        work_matrix[j-1].append(i-1)
    # 방문체크 배열
    visited = [False] * n
    # x: 오늘 반드시 끝내야하는 작업 -> 인덱스는 0부터 시작하므로 -1
    x = int(input()) - 1

    # print(work_matrix)
    # print(visited)
    # print(x)

    count = 0

    def dfs(current):
        global count
        # 방문한 지점 표시
        visited[current] = True

        for i in work_matrix[current]:
            if not visited[i]:
                count += 1
                dfs(i)

    dfs(x)
    print(count)
    '''