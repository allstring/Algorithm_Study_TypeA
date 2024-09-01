# 감시 피하기
# Gold V
# https://www.acmicpc.net/problem/18428

def is_safe(hall: list, teachers: list):
    """
    is_safe() 함수는 현재 복도 상태에서 모든 학생이 감시를 피할 수 있는지 확인하는 함수이다.
    :param hall: 장애물이 3개 놓인 현재 복도 정보
    :param teachers: 선생님 좌표 리스트
    :return: 모든 학생이 선생님의 감시를 피할 수 있으면 True, 그렇지 않으면 False를 반환
    """
    for t_row, t_col in teachers:
        for dr, dc in directions:  # 감시 가능한 방향에 대해서
            obs_flag = False  # 현 방향에 장애물 여부
            next_t_row = t_row  # 현 방향 다음 칸 (초기는 현재 위치)
            next_t_col = t_col  # 현 방향 다음 칸 (초기는 현재 위치)
            while 0 <= next_t_row + dr < N and 0 <= next_t_col + dc < N:
                if obs_flag:
                    # 장애물 혹은 다른 선생님이 있다면 현 방향 확인 중단
                    break
                next_t_row += dr  # 현 방향으로 한 칸 전진
                next_t_col += dc  # 현 방향으로 한 칸 전진
                if hall[next_t_row][next_t_col] == "S":
                    # 해당 방향에 학생이 보이는 경우
                    return False
                elif hall[next_t_row][next_t_col] == "O" or hall[next_t_row][next_t_col] == "T":
                    # 전진한 칸에 장애물 혹은 다른 선생님이 있는 경우
                    obs_flag = True

    return True


def dfs(hall, obs_cnt):
    """
    dfs() 함수는 현재 복도 상태를 기준으로 새로운 장애물을 설치하는 재귀 함수이다.
    :param hall: 복도 정보
    :param obs_cnt: 현재 복도에 존재하는 장애물 개수
    :return: None
    """
    global safe_flag  # 복도 안전 여부 (감시를 피할 수 있는 경우)

    if obs_cnt == 3:
        # 장애물 개수가 3개(최대)인 경우 
        if is_safe(hall, teachers):
            # 힉셍들이 모든 감시를 피할 수 있는 경우
            safe_flag = True
            return
        else:
            # 학생들이 모든 감시를 피할 수 없는 경우
            return

    # 모든 좌표에 대해서 순회
    for i in range(N):
        for j in range(N):
            if hall[i][j] == "X":
                # 빈 복도인 경우
                hall[i][j] = "O"  # 장애물 설치
                dfs(hall=hall, obs_cnt=obs_cnt + 1)  # 장애물 설치 후 재귀
                if safe_flag:
                    # 감시를 모두 피할 수 있는 경우가 있을 경우 반복문 종료
                    break
                # 감시를 피할 수 있는 경우가 없었다면, 현재 위치 장애물을 제거 후 반복문 진행
                hall[i][j] = "X"  # 장애물 설치 원복
        if safe_flag:
            # 감시를 모두 피할 수 있는 경우가 있을 경우 반복문 종료
            break


N = int(input())  # 복도(행렬) 크기, 3 <= N <= 6

hall = []  # 복도 배열
teachers = []  # 선생님 좌표 리스트
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 선생님 감시 방향
init_obs_cnt = 0
safe_flag = False

# 복도 정보 입력
for r in range(N):
    row = list(input().split())
    hall.append(row)
    for c in range(len(row)):
        if row[c] == "T":  # 선생님 좌표 (i, j)
            teachers.append([r, c])

# 초기 상태로 dfs 진행
dfs(hall, init_obs_cnt)

if safe_flag:
    print("YES")
else:
    print("NO")
