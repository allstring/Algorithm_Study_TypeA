# 토마토
# Gold V
# bfs


"""
풀이 설명:
    두 개의 스택을 사용하여 BFS로 구현.
    DAY에 익은 토마토 좌표를 구한 뒤,
    DAY+1에 익을 예정인 토마토 좌표들을 구해서 메인 스택(ripe_tomatoes)이 모두 빌 때까지 반복
"""


def is_valid(pos):
    r, c = pos[0], pos[1]

    # 좌표 유효성 검사
    if r < 0 or r >= N or c < 0 or c >= M:
        return False
    # 트뭬이러 췍
    if box[r][c] != 0:
        return False

    return True


def is_all_ripe():
    """
    박스 내 토마토가 모두 익었는지 확인하는 함수
    """

    # (N*M)-(2*EMPTY)의 이유:
    # 빈 칸의 경우 -1로 채워지기 때문에,
    # 빈 칸의 개수 두 배에 해당 하는 값을 빼주어야 박스 내 익은 토마토 개수를 셀 수 있다.
    if sum([sum(row) for row in box]) == ((N*M)-(2*EMPTY)):
        print(DAY)
        return
    else:
        print(-1)
        return


def main():
    global N, M, box, EMPTY, DAY

    M, N = map(int, input().split())  # N x M 상자의 크기 [2, 1000] -> D 금지
    box = [list(map(int, input().split())) for _ in range(N)]

    # 저장될 때부터 모든 토마토가 익어있는 상태 -> 바로 컽
    if sum([sum(row) for row in box]) == N * M:
        print(0)
        return

    ripe_tomatoes = list()  # 익은 토마토들의 좌표

    # 박스 순회 -> 초기에 익은 토마토 좌표 검색 및 빈 칸 카운팅
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:  # 익은 토마토
                ripe_tomatoes.append((r, c))
            elif box[r][c] == -1:  # 빈 칸
                EMPTY += 1

    # 'B'FS (스택 두 개 사용)
    while ripe_tomatoes:
        DAY += 1
        tmp_stack = list()

        # DAY에 익은 토마토 좌표
        while ripe_tomatoes:
            tomato = ripe_tomatoes.pop()
            r, c = tomato[0], tomato[1]
            dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

            for dr, dc in dir_:
                nr = r + dr
                nc = c + dc
                if is_valid((nr, nc)):
                    box[nr][nc] = 1  # DAY+1에 익은 토마토 좌표
                    tmp_stack.append((nr, nc))  # 임시 스택 저장

        ripe_tomatoes = tmp_stack  # 익은 토마토 좌표 업데이트

    is_all_ripe()  # 모든 토마토가 익었는지 확인


if __name__ == "__main__":
    # GLOBAL 변수
    N, M = 0, 0
    box = []
    EMPTY = 0
    DAY = -1

    main()