# 1890. 점프

import sys
sys.stdin = open("input.txt", "r")

def find_road_count(dp, n):
    for i in range(n):
        for j in range(n):
            # 갈 수 있는 거리가 0이고 마지막 위치 아닌 경우
            if game_board[i][j] == 0 and (i, j) == (n-1, n-1):
                continue
            # 오른쪽이나 아래로 이동
            dxy = [(0, 1), (1, 0)]
            for dx, dy in dxy:
                # 오른쪽이나 아래로 game_board 값만큼 이동
                x, y = i + dx * game_board[i][j], j + dy * game_board[i][j]
                # game_board 범위를 벗어나는 경우
                if not (0 <= x <= n - 1 and 0 <= y <= n - 1):
                    continue
                # 이동 가능한 경로의 개수 합쳐주기
                dp[x][y] += dp[i][j]
    # dp의 마지막 도착 위치 값 반환
    return dp[-1][-1]

# n: 게임 판의 크기
n = int(input())

# game_board: 게임 판(0 <= 칸에 적혀있는 수 <= 9)
game_board = [list(map(int, input().split())) for _ in range(n)]
# dp: 경로의 개수 배열
dp = [[0] * n for _ in range(n)]
# 시작 지점은 개수 1개로 설정
dp[0][0] = 1

result = find_road_count(dp, n)
print(result)