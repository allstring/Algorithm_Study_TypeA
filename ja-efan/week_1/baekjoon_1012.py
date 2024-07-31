# 유기농 배추
# Silver II
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque

# 빠른 입출력
inputf = sys.stdin.readline
printf = sys.stdout.write

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    # M: 배추밭 가로 길이
    # N: 배추밭 세로 길이
    # K: 배추 위치 개수 (배추 개수)
    M, N, K = map(int, inputf().rstrip().split())

    # 배추밭 0으로 초기화
    cabbage_field = [[0 for _ in range(M)] for _ in range(N)]

    # 배추가 심어진 좌표 갱신
    for _ in range(K):
        c, r = map(int, inputf().rstrip().split())  # 배추 심어진 좌표 정보
        # print(r, c)
        cabbage_field[r][c] = 1

    # 배추밭 좌표 방문 여부 체크 리스트
    visited = [[False for _ in range(M)] for _ in range(N)]
    warm_cnt = 0

    # 지렁이가 움질일 수 있는 방향
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # 모든 좌표 순회
    for r in range(N):
        for c in range(M):
            # 방문 했거나, 배추가 심어져 있지 않은 좌표인 경우 다음 좌표 순회
            if visited[r][c] or cabbage_field[r][c] == 0:
                continue
            # 배추가 심어진 좌표를 큐에 추가
            queue = deque([(r, c)])
            # 현재 좌표 방문 체크
            visited[r][c] = True
            # 큐가 빌 때까지 반복
            while queue:
                # 좌표 하나 꺼내 주고,
                row, col = queue.popleft()
                # 지렁이가 이동 가능한 4 방향에 대한 순회
                for dr, dc in directions:
                    # 다음 좌표
                    nr, nc = row + dr, col + dc
                    # 다음 좌표 유효성 검사 (밭을 벗어나는지, 배추가 심어져 있는지, 방문 하지 않았는지)
                    if 0 <= nr < N and 0 <= nc < M and cabbage_field[nr][nc] == 1 and not visited[nr][nc]:
                        # 만족 한다면 방문 체크
                        visited[nr][nc] = True
                        # 큐에 추가
                        queue.append((nr, nc))

            # 지렁이가 옮겨 다닐 수 있는 배추 군집 하나 추가
            warm_cnt += 1

    # 결과 출력
    printf(f"{warm_cnt}\n")
