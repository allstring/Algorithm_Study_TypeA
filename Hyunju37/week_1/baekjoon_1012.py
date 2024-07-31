T = int(input())


def get_warms(M, N, farm, i, j):
    global visited
    #종료 조건들~~~~~~~~~~~~~~~~~~~~
    if i < 0 or i >= M or j < 0 or j >= N: return # 경계값 처리(가장먼저!!)
    if farm[i][j] == 0: return  #1 영역 벗어남
    if visited[i][j]: return #이미 방문한 곳
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)] #4방향 정의(문제에서 정의하는 '인접'의 기준)
    visited[i][j] = True #방문처리

    for dx, dy in dxy: #4방향 이동해서 확인하기
        nx = i + dx
        ny = j + dy
        #이 줄(아래)을 추가해줬더니 RecursionError 나지 않았다.
        #DFS를 또 호출하기 전에 경계를 이미 벗어나는 경우들을 미리 가지치기 해줌으로써
        #재귀호출 스택을 아낄 수 있는것?
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        get_warms(M, N, farm, nx, ny) #DFS 호출(이동 방향에서 깊이 들어가서 탐색)

for t in range(T):
    M, N, K = map(int, input().split())
    # M x N 배열 초기화
    farm = [[0]*N for _ in range(M)]

    for _ in range(K):
        i, j = map(int, input().split())
        farm[i][j] = 1


    warm_cnt = 0 #필요한 지렁이의 개수
    visited = [[False]*N for _ in range(M)] #방문여부 저장할 배열

    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and not visited[i][j]: #아직 방문하지 않은 '1'영역 발견
                get_warms(M, N, farm, i, j) # DFS 탐색
                warm_cnt += 1 #지렁이 개수 카운트
    print(warm_cnt)
