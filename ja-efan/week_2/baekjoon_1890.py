# 점프
# Silver I
# https://www.acmicpc.net/problem/1890

"""
풀이 설명 :
    (0,0)을 시작으로 이동 가능한 모든 좌표에 대해서,
    해당 좌표까지의 경로 개수를 모두 저장한다. (memoization)
    좌표 접근 방법 개수를 갱신하며 (N-1, N-1) 좌표에 도달하면 모든 memo가 끝난다.
    이때, memo 리스트의 (N-1, N-1) 좌표 값이 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로
    규칙에 맞게 이동할 수 있는 경로의 수가 된다.

"""

def main():
    N = int(input())  # 게임판의 크기
    game_board = [list(map(int, input().split())) for _ in range(N)]

    # (r,c) 좌표까지 경로의 수를 기록
    memo = [[0 for _ in range(N)] for _ in range(N)]
    memo[0][0] = 1  # 초기 위치 (0,0) 값을 1로 초기화

    for r in range(N):
        for c in range(N):
            j = game_board[r][c]
            if j == 0:  # 종착점
                continue
            # 반드시 오른쪽이나 아래쪽으로만 이동하기에 0이하로 내려갈 일이 없음
            if r + j < N :  # 아래쪽 이동
                memo[r+j][c] += memo[r][c]  # 다음 좌표에 현재 좌표의 memo 값 추가
            if c + j < N :  # 오른쪽 이동
                memo[r][c+j] += memo[r][c]  # 다음 좌표에 현재 좌표의 memo 값 추가

    print(memo[-1][-1])  # 마지막 좌표 경로 개수 출력


if __name__ == "__main__":
    main()