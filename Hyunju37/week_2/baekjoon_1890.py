
def count_number_of_paths(board):
    n = len(board)
    # 각 좌표마다 reachable 한 way가 몇 개인지를 저장할 배열 초기화
    reach_ways = [[0] * n for _ in range(n)]
    reach_ways[0][0] = 1

    target = (n-1, n-1) #목적지 좌표

    for i in range(0, n):
        for j in range(0, n):
            if i == n-1 and j == n-1:
                break
            jump = board[i][j]
            if i + jump < n:
                reach_ways[i+jump][j] += reach_ways[i][j]
            if j + jump < n:
                reach_ways[i][j+jump] += reach_ways[i][j]

    return reach_ways[n-1][n-1]

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(count_number_of_paths(board))

if __name__ == '__main__':
    main()