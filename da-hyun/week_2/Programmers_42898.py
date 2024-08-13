def solution(m, n, puddles):
    answer = 0
    DP = [[0] * m for _ in range(n)]  # DP 테이블 초기화 (모든 값 0으로)
    DP[0][0] = 1  # 시작점 초기화
    que = [(0, 0)]  # BFS를 위한 큐 초기화
    while que:
        x, y = que.pop(0)  # 큐에서 좌표 추출
        DP[x][y] %= 1000000007  # 모듈러 연산 적용
        if([y + 1, x + 1] in puddles):  # 물 웅덩이 확인
            continue
        if 0 <= x + 1 < n and 0 <= y < m:  # 아래로 이동 가능할 경우
            if not DP[x + 1][y]:  # 아직 방문하지 않은 곳이면 큐에 추가
                que.append((x + 1, y))
            DP[x + 1][y] += DP[x][y] % 1000000007  # 현재 위치의 값을 다음 위치에 더함
        if 0 <= x < n and 0 <= y + 1 < m:  # 오른쪽으로 이동 가능할 경우
            if not DP[x][y + 1]:  # 아직 방문하지 않은 곳이면 큐에 추가
                que.append((x, y + 1))
            DP[x][y + 1] += DP[x][y] % 1000000007  # 현재 위치의 값을 다음 위치에 더함
    return(DP[n-1][m-1])  # 도착점의 값을 반환
