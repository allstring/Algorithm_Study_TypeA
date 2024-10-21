# 17070. 파이프 옮기기

import sys
sys.stdin = open('input.txt', 'r')

'''
    문제유형 파악 :
    처음에는 dfs로 해결을 하고자 하였으나 집의 크기가 16까지 있기 때문에 층이 너무 깊어짐
    또한, 모든 경우를 따지기에는 점화식 형태가 적절하다고 생각됨 -> DP
    
    문제풀이 :
    처음에는 dp를 이동시키는 경우의 수로 설정
    -> 가로, 세로, 대각선의 움직임을 표현할 수 있는 경우의 수가 너무 많아지는 느낌이었음
    -> 식을 세우기 쉽지 않았기 때문에 포기
    문제해결을 위해서 검색을 통해 기본적인 idea를 참고함
    -> dp를 [가로, 세로, 대각선]으로 이동시키는 형태로 만들 수 있음을 확인
    -> 이 아이디어만 참고하여 문제풀이 진행하였고, 경우의 수와 조건을 따져 dp 함수 생성
    -> 벽에 막히는 경우의 수를 계속 시험해보며 문제 해결
'''

def main():
    T = int(input())

    for _ in range(T):
        # N: 집의 크기 (3 <= N <= 16)
        N = int(input())
        # houses: 집의 상태 리스트 (0: 빈 칸, 1: 벽)
        # (1, 1)과 (1, 2)는 항상 빈 칸
        houses = [list(map(int, input().split())) for _ in range(N)]
        # dp: 위치별로 이동시키는 방법의 개수 (오른쪽, 아래, 오른쪽 아래 대각선)
        dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

        # 첫 번째 행의 경우에는 오른쪽으로 이동하는 경우밖에 없음
        for i in range(N):
            if houses[0][i] == 0:
                dp[0][i][0] = 1

        def find_pipe(houses, dp):
            
            # 모든 경우를 돌면서 파이프 이동
            for x in range(N):
                # 출발을 가로로 시작하기 때문에 2개의 열에는 이동이 불가능
                # 따라서, 2부터 시작
                for y in range(2, N):
                    # 만약 이동하려는 위치에 벽이 있는 경우
                    if houses[x][y] == 1:
                        continue

                    # 파이프가 가로로 움직이는 경우
                    dp[x][y][0] = dp[x][y - 1][0] + dp[x][y - 1][2]

                    # 파이프가 세로로 움직이는 경우
                    dp[x][y][1] = dp[x-1][y][1] + dp[x-1][y][2]

                    # 파이프가 대각선으로 움직이는 경우
                    # 이 경우에는 2칸의 조건이 추가되므로 if문을 통해 해결
                    if houses[x-1][y] == 0 and houses[x][y-1] == 0:
                        dp[x][y][2] = dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]

            return sum(dp[-1][-1])

        result = find_pipe(houses, dp)
        print(result)

if __name__ == "__main__":
    main()

''' 오른쪽, 아래, 오른쪽 아래 대각선 방향을 구분하기가 어려움
def main():
    T = int(input())
    
    for _ in range(T):
        # N: 집의 크기 (3 <= N <= 16)
        N = int(input())
        # houses: 집의 상태 리스트 (0: 빈 칸, 1: 벽)
        # (1, 1)과 (1, 2)는 항상 빈 칸
        houses = [list(map(int, input().split())) for _ in range(N)]
        # dp: 위치별로 이동시키는 방법의 개수
        dp = [[0] * N for _ in range(N)]

        # dxy: 오른쪽, 아래, 오른쪽 아래 대각선 방향
        dxy = [[0, 1], [1, 0], [1, 1]]

        def dp(houses, dp, start_x, start_y, end_x, end_y):

            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    # 만약 첫 줄이라면, 이동시키는 방법의 개수는 1
                    if x == 0:
                        dp[x][y] = 1
                    if y == 1:
                        dp[x][y] = 1

                    dp[x][y] = dp[x-1][y] + dp[x-2][y-1] + dp[x][y-1] + dp[x-1][y-2] + dp[x-1][y-1]

            return dp[-1][-1]

        result = dp(houses, dp, 0, 1, N, N)
        print(result)

if __name__ == "__main__":
    main()
'''