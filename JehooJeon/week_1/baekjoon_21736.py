# 21736. 헌내기는 친구가 필요해

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(campus, start, visited):
    # 만난 사람 수 변수 정의
    total_people = 0
    
    # 출발 지점 위치값 1
    visited[start[0]][start[1]] = 1
    # 출발 지점 queue 추가
    queue = deque([(start[0], start[1])])

    # 상, 하, 좌, 우
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # queue가 없을 때까지 반복
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 범위 내 아닐 경우 continue
            if not (0 <= nx < n and 0 <= ny < m): continue

            # 이미 방문한 곳이면 continue
            if visited[nx][ny] == 1: continue

            # 사람을 만났을 때
            if campus[nx][ny] == 'P':
                # 만난 사람 수 +1
                total_people += 1
                # 이미 만난 사람은 'O'로 바꾸기
                campus[nx][ny] = 'O'
                queue.append((nx, ny))
                # 방문한 위치값 1로 바꾸기
                visited[nx][ny] = 1
            # 빈공간일 때
            elif campus[nx][ny] == 'O':
                queue.append((nx, ny))
                visited[nx][ny] = 1
            # X(벽)를 만날 경우 continue
            else:
                continue
    
    # 만난 사람 없을 경우 TT 출력
    if total_people == 0:
        return "TT"
    return total_people

T = int(input())

for _ in range(T):
    # n, m: 캠퍼스의 크기
    n, m = map(int, input().split())
    campus = [list(input()) for _ in range(n)]
    # 방문한 위치 표시하기 위한 리스트 정의
    visited = [[0] * m for _ in range(n)]
    # print(campus)
    
    # 도연이가 출발하는 지점 좌표를 start에 저장
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                start = (i, j)
    
    # bfs를 통해 result 값 출력
    result = bfs(campus, start, visited)

    print(result)



