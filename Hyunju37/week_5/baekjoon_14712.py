def main():
    def valid(r, c):
        if r > 0 and c > 0:
            if grid[r][c] == 1 and grid[r-1][c] == 1 and grid[r][c-1] == 1 and grid[r-1][c-1] == 1:
                return False
        return True
    def nemmo(idx):
        if idx == N * M:
            return 1
        r = idx // M
        c = idx % M
        total_ways = 0
        grid[r][c] = 1
        if valid(r,c):
            total_ways += nemmo(idx+1)
        grid[r][c] = 0
        total_ways += nemmo(idx+1)
        return total_ways



    N, M = list(map(int, input().split()))
    grid = [[0]*M for _ in range(N)]
    ans = nemmo(0)
    print(ans)

if __name__ == "__main__":
    main()