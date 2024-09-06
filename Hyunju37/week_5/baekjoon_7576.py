from collections import deque

def main():

    def spread_bfs(grid):
        if not any(0 in row for row in grid):
            return 0 #저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
        steps = 0 #BFS의 depth를 의미하는 변수

        while queue:
            steps += 1 #depth가 같은 셀들을 탐색할 때마다 step값 증가시키기
            for _ in range(len(queue)): #큐에 있는 좌표들을 한꺼번에 탐색
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                        grid[nx][ny] = steps #step표시
                        queue.append((nx, ny))

        if any(0 in row for row in grid):
            return -1 #토마토가 모두 익지는 못하는 상황이면 -1을 출력

        return max([max(row) for row in grid]) #모두 익은 경우 step의 max값을 출력

    N, M = map(int, input().split())
    tomatos = [list(map(int, input().split())) for _ in range(M)]
    ans = spread_bfs(tomatos)
    print(ans)

if __name__ == "__main__":
    main()