def is_valid(x, y, N, board, DP):
    # 주어진 좌표 (x, y)에서 목적지까지 갈 수 있는 경로의 수를 계산하는 함수
    tmpAnswer = 0
    if x < 0 or x >= N or y < 0 or y >= N: return 0  # 좌표가 보드 범위를 벗어나면 0 반환
    if DP[x][y] != -1: return DP[x][y]  # 이미 계산된 경로 수가 있으면 그 값 반환
    tmpValue = board[x][y]
    if tmpValue == 0: return 0  # 현재 위치의 값이 0이면 이동 불가
    tmpAnswer += is_valid(x + tmpValue, y, N, board, DP)  # 오른쪽으로 이동
    tmpAnswer += is_valid(x, y + tmpValue, N, board, DP)  # 아래로 이동
    DP[x][y] = tmpAnswer  # 계산된 경로 수를 DP에 저장
    return tmpAnswer 

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)] 
    DP = [[-1] * N for _ in range(N)]
    DP[N-1][N-1] = 1  # 목적지에서 경로의 수는 1로 설정
    is_valid(0, 0, N, board, DP)  # 시작점에서 목적지까지의 경로 수 계산
    print(DP[0][0])

if __name__ == "__main__":
    main()