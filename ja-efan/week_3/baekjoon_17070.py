# 파이프 옮기기 1
# Gold V
# https://www.acmicpc.net/problem/17070

from pprint import pprint


def check_walls(r,c, house):

    pre_directions = [[0, -1], [-1, 0]]
    for pre_r, pre_c in pre_directions:
        if house[r+pre_r][c+pre_c] == 1:
            return False
    return True

def main():
    N = int(input()) # 집의 크기 (3 <= N <= 16)
    house = [list(map(int, input().split())) for _ in range(N)]
    memo = [[[0,0,0] for _ in range(N)] for _ in range(N)]

    # base case
    # 첫 번째 행
    for i in range(1, N):
        if house[0][i] == 1:
            break
        memo[0][i]  = [1, 0, 0]

    pre_directions = [[0, -1], [-1, -1], [-1, 0]]  # 이전 파이프의 상대적인 위치 (좌,좌측 위, 위)
    for r in range(1, N):
        for c in range(2, N):

            if house[r][c] == 1:
                continue
            # pre_sum = 0
            if r == 1:
                for i, pre_d in enumerate(pre_directions[:2]): # 왼쪽과 왼쪽 위만 확인
                    pre = memo[r + pre_d[0]][c + pre_d[1]]
                    if i == 1:  # 왼쪽 위(대각선)에서 접근 -> 모든 방향 수용 가능
                        if check_walls(r, c, house):
                            memo[r][c][i] += sum(pre)
                    else :
                        memo[r][c][i] += sum(pre)
            else :
                for i, pre_d in enumerate(pre_directions):
                    pre = memo[r + pre_d[0]][c + pre_d[1]]
                    if i == 0:  # 왼쪽에서 접근 -> 이전 메모의 위쪽 count 제외 -> [:2]
                        memo[r][c][i] += sum(pre[:2])
                    elif i == 1:  # 왼쪽 위(대각선)에서 접근 -> 모든 방향 수용 가능
                        if check_walls(r, c, house):
                            memo[r][c][i] += sum(pre)
                    elif i == 2:  # 위에서 접근
                        memo[r][c][i] += sum(pre[1:])

    # pprint(memo)
    pprint(sum(memo[-1][-1]))
if __name__ == "__main__":
    main()