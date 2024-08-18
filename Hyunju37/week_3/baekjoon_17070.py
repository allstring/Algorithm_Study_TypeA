
'''
이동가능한 방향은 아래, 오른쪽, 우하향대각 3가지 뿐
도착 지점은 무조건 세로면 아래쪽, 가로면 오른쪽, 대각이면 우하단에 위치할 것
굳이 매번 두 개의 좌표값을 고려할 필요 없다.
세로 파이프의 경우 아래쪽, 가로 파이프의 경우 오른쪽, 대각 파이프의 경우 오른쪽 아래 좌표
만 고려하면 된다.
'''
def main():
    N = int(input())
    house = [list(map(int, input().split())) for _ in range(N)]

    #dynamic programming
    #3 channels NxN array -각각 그 위치에서 가로/세로/대각
    #[][][0] 가로
    #[][][1] 세로
    #[][][2] 대각
    pipe_cnt = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

    #초기 위치 (0,1) - 가로 방향으로 놓여 있음
    pipe_cnt[0][1][0] = 1

    #0행 초기화 - 가로 방향으로만 연속해서 이동할 때만 가능하므로 따로 처리
    for j in range(2, N):
        if house[0][j] == 0:
            pipe_cnt[0][j][0] = pipe_cnt[0][j - 1][0]

    for i in range(1, N): #0행은 앞에서 이미 처리함
        for j in range(2, N): #0열과 1열 도달 불가능. (초기 상황에서의 1열 빼고)
            #그 자리에 대각선으로 놓일 수 있는경우 - from 가로 or 세로 or 대각
            if house[i][j] == house[i][j-1] == house[i-1][j] == 0:
                pipe_cnt[i][j][2] = sum(pipe_cnt[i-1][j-1])
            #그 자리에 가로 또는 세로로 놓일 수 있는 경우
            if house[i][j] == 0:
                pipe_cnt[i][j][0] = pipe_cnt[i][j-1][0] + pipe_cnt[i][j-1][2] #가로 - from 가로 or 대각
                pipe_cnt[i][j][1] = pipe_cnt[i-1][j][1] + pipe_cnt[i-1][j][2] #세로 - from 세로 or 대각

    print(sum(pipe_cnt[N-1][N-1]))




if __name__== '__main__':
    main()