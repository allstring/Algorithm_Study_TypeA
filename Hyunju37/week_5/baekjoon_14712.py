def main():
    def valid(r, c): #2x2 있는지 체크
        if r > 0 and c > 0:
            if grid[r][c] == 1 and grid[r-1][c] == 1 and grid[r][c-1] == 1 and grid[r-1][c-1] == 1:
                return False
        return True
    def nemmo(idx): #idx는 1D배열상에서의 인덱스
        if idx == N * M:
            return 1 #모든 경우 탐색 완료
        r = idx // M #행
        c = idx % M #열
        total_ways = 0 #카운트 초기화
        grid[r][c] = 1 #1) 현재 셀에 넴모를 놓는다.
        if valid(r,c): #valid한 경우 카운트 더하기
            total_ways += nemmo(idx+1)
        grid[r][c] = 0 #2) 현재 셀에 넴모를 놓지 않는다.
        total_ways += nemmo(idx+1) #카운트 더하기
        return total_ways



    N, M = list(map(int, input().split()))
    grid = [[0]*M for _ in range(N)]
    ans = nemmo(0)
    print(ans)

if __name__ == "__main__":
    main()