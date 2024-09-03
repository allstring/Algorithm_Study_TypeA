
def main():
    N, M = list(map(int, input().split()))
    above = [list(map(int, input().split())) for _ in range(N)] #N x M
    front = list(map(int, input().split())) #M
    right = list(map(int, input().split())) #N

    blocks = [row[:] for row in above] #일단 위에서 본 모습으로 초기화

    for j, colmax in enumerate(front): #front 배열 기준으로 빈 위치가 아닌 곳을 열 최댓값으로 채워넣기
        for i in range(N):
            if blocks[i][j] == 1:
                blocks[i][j] = colmax

    for i, rowmax in enumerate(right[::-1]): #right 배열은 row max 값을 의미하므로 각 행에서 row max를 초과하는 값을 맞춰줌
        for j in range(M):
            if blocks[i][j] > rowmax:
                blocks[i][j] = rowmax

    for col in range(M): #쌓기나무 성립불가능 판별, 각 열 max높이 확인
        real_colmax = max(blocks[i][col] for i in range(N))
        if real_colmax != front[col]:
            print(-1)
            return

    for row in range(N): #쌓기나무 성립불가능 판별, 각 행 max높이 확인
        real_rowmax = max(blocks[row])
        if real_rowmax != right[::-1][row]:
            print(-1)
            return

    for i in range(N):
        for j in range(M):
            print(blocks[i][j], end= ' ')
        print()

if __name__ == '__main__':
    main()