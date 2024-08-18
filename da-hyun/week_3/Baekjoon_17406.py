import itertools

# 회전 방향에 따라 인덱스를 계산하는 함수
def turnIndex(r, c, i, j):
    if r == i and c == j: return (i, j)  # 현재 위치와 목표 위치가 같으면 그대로 반환
    if abs(r - i) == abs(c - j):  # 대각선일 경우
        if r > i and c > j: return (i+1, j)
        if r > i and c < j: return (i, j-1)
        if r < i and c > j: return (i, j+1)
        if r < i and c < j: return (i-1, j)
    if abs(r-i) > abs(c-j):  # 세로 방향이 더 긴 경우
        if r > i: return (i, j-1)
        if r < i: return (i, j+1)
    if abs(r-i) < abs(c-j):  # 가로 방향이 더 긴 경우
        if c > j: return (i+1, j)
        if c < j: return (i-1, j) 
    return (0, 0)

def main():
    N, M, K = map(int, input().split())  # 행, 열, 회전 횟수 입력
    pre_board = [list(map(int, input().split())) for _ in range(N)]  # 초기 보드 상태 입력
    turnList = [list(map(int, input().split())) for _ in range(K)]  # 회전 정보 입력
    allList = itertools.permutations(turnList, K)  # 회전 순서의 모든 조합 생성
    board = [[0]* M for _ in range(N)]
    answer = 5001  # 최소 값을 저장할 변수 초기화
    for tmpTurn in allList:
        for i in  range(N):
            for j in range(M):
                tmp_i, tmp_j = i, j
                for k in range(K-1, -1, -1):
                    r, c, s = tmpTurn[k]
                    r, c = r-1, c-1
                    if r-s <= tmp_i <= r+s and c-s <= tmp_j <= c+s:
                        tmp_i, tmp_j = turnIndex(r, c, tmp_i, tmp_j)
                board[i][j] = pre_board[tmp_i][tmp_j]
        answer = min(answer, min([sum(row) for row in board]))  # 최소 값을 갱신
    print(answer)  # 최소 결과 출력

if __name__ == "__main__":
    main()
