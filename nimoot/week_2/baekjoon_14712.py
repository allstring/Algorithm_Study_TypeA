def dfs(cx, cy, nemmo): # 현재 좌표(cx,cy), nemmo 배열
    if cx == row: # 행 범위 넘어가면 종료
        return 1

    if cy == col: # 열 범위 넘어가면 다음 행으로 이동
        return dfs(cx + 1, 0, nemmo)

    # 넴모 안놓고 dfs 실행
    count = dfs(cx, cy + 1, nemmo)

    # 넴모 놓을 수 있는지 확인
    if cx > 0 and cy > 0 and nemmo[cx - 1][cy] == 1 and nemmo[cx][cy - 1] == 1 and nemmo[cx - 1][cy - 1] == 1:
        return count # 넴모 못넣으니까 count 반환

    # 넴모 놓고 dfs 실행
    nemmo[cx][cy] = 1
    count += dfs(cx, cy + 1, nemmo)
    nemmo[cx][cy] = 0

    return count

row, col = map(int, input().split())
nemmo = [[0] * col for _ in range(row)]
result = dfs(0, 0, nemmo)
print(result)
    