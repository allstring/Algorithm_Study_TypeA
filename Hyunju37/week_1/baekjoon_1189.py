from collections import deque

def find_paths(road, r, c, k):
    #4방향 정의
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    #이동 가능한 곳인지 체크 (경계조건, 이미 방문하지는 않았는지, T가 아닌지)
    def is_valid(x, y, visited, raod):
        return 0<=x<r and 0<=y<c and not visited[x][y] and road[x][y] == '.'


    def dfs(x, y, moves, visited):
        if x == 0 and y == c-1: #도착했고 딱 거리가 K인 경로였다면
            return 1 if moves == K else 0

        if moves >= K: #K를 넘어감
            return 0

        visited[x][y] = True #방문처리
        paths_count = 0 #경로의 개수 초기화
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited, road):
                paths_count += dfs(nx, ny, moves + 1, visited) #이동한 곳에서부터 DFS호출

        visited[x][y] = False #backtracking
        return paths_count

    visited = [[False]*c for _ in range(r)]
    return dfs(r-1,0,1,visited)


R, C, K = map(int, input().split())
road = [list(input()) for _ in range(R)]

print(find_paths(road, R, C, K))
