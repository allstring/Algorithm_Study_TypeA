# 7576. 토마토

# import sys
# sys.stdin = open('baekjoon_7576_input.txt', 'r')

from collections import deque

def main():
    def bfs(queue):
            while queue:
                x, y = queue.popleft()

                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy

                    # 범위를 벗어나는 경우
                    if not (0 <= nx < N and 0 <= ny < M): continue
                    # 익지않은 토마토의 위치가 아닌 경우
                    if tomatoes[nx][ny] != 0: continue

                    tomatoes[nx][ny] = tomatoes[x][y] + 1
                    queue.append((nx, ny))
            return
    
    # 모든 칸을 돌면서 익지 않은 토마토가 존재하면 -1 출력
    # 모든 토마토가 익어있는 상태 -> 최댓값이 1인 경우 0 출력
    # 나머지 경우에는 최댓값 - 1(시작값 = 1) => 즉, 익지 않은 토마토가 존재하는 경우 제외하고는 최댓값 -1 출력
    def find_tomato(tomatoes):
        max_cnt = 1
        for i in range(N):
            for j in range(M):
                if tomatoes[i][j] == 0:
                    return -1
                max_cnt = max(max_cnt, tomatoes[i][j])
        return max_cnt - 1

    # 우, 하, 상, 좌
    dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    # M, N: 상자의 가로 칸의 수, 세로 칸의 수
    # 2 <= M, N <= 1,000
    M, N = map(int, input().split())
    # tomatoes: 상자에 저장된 토마토들의 정보 리스트
    tomatoes = [list(map(int, input().split())) for _ in range(N)]
    # queue: 익은 토마토 위치 넣을 큐
    queue = deque([])

    # 토마토가 익어있는 위치 좌표
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append([i, j])

    # 모든 익어있는 토마토를 돌면서 bfs 수행
    bfs(queue)

    # 최종 결과 출력
    result = find_tomato(tomatoes)
    print(result)
        
if __name__ == '__main__':
    main()