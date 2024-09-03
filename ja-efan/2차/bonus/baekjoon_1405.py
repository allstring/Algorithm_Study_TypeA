# 미친 로봇
# Gold IV
"""
풀이 설명:
    로봇이 동서남북으로 움직일 수 있는 최대 크기의 맵을 설정해주고,
    해당 맵에서 dfs를 활용해 이동 확률을 구해준다.
    로봇의 이동 횟수가 입력으로 주어진 N과 동일하다면, 이동 확률을 더해주고 반환.
"""

def main():
    """
    N: 로봇의 이동 횟수 [1, 14]
    prob_x: x 방향으로 이동할 확률
    """
    N, prob_e, prob_w, prob_s, prob_n = map(int, input().split())  # 문제 입력

    # 이동이 움직일 수 있는 좌표이자, 방문 여부 체크 리스트
    visited = [[False for _ in range(29)] for _ in range(29)]

    # 동 서 남 북 방향으로 움직일 확률
    probability_list = [prob_e, prob_w, prob_s, prob_n]

    # 경로가 단순할 확률을 누적시킬 변수
    global total_probability

    def dfs(n: int, curr_position: tuple, probability: float):
        """
        로봇의 이동을 진행시키는 dfs 함수

        :param n: 현재까지 로봇이 이동한 칸 수
        :param curr_position: 현재 로봇의 위치
        :param probability: 현재 위치까지 로봇이 도달할 확률
        :return: None
        """
        global total_probability
        if n == N:
            # 주어진 이동 횟수를 모두 채운 경우
            # 현재 위치까지의 이동 확률을 누적해주고, 리턴
            total_probability += probability
            return

        # 로봇이 움직이는 방향, 동 서 남 북
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        curr_r = curr_position[0]  # 현재 로봇의 좌표(행)
        curr_c = curr_position[1]  # 현재 로봇의 좌표(열)

        # 다음 이동 방향과 이동 확률
        for dir_, next_prob in zip(directions, probability_list):
            next_r = curr_r + dir_[0]  # 다음 좌표(행)
            next_c = curr_c + dir_[1]  # 다음 좌표(열)

            # 다음 좌표 유효성 검사 (로봇이 움직일 수 있는 범위는 visited 범위와 동일)
            if next_r < 0 or next_r >= len(visited) or next_c < 0 or next_c >= len(visited):
                continue
            # 다음 좌표 방문 여부 검사: 방문한 적이 있다 -> 단순 경로 생성이 불가능하다.
            if visited[next_r][next_c]:
                continue
            # 다음 좌표 방문 체크
            visited[next_r][next_c] = True

            # 다음 좌표 기준 dfs 재귀 호출, 현재까지 확률에 다음 이동 확률 곱해준다.
            dfs(n + 1, (next_r, next_c), probability*(0.01*next_prob))

            # 다음 좌표 방문 원복
            visited[next_r][next_c] = False

    # 초기 설정 값
    init_n = 0  # 로봇의 이동 횟수
    init_pos = (14, 14)  # 초기 위치는 중앙
    init_probability = 1  # 초기 확률 값
    visited[init_pos[0]][init_pos[1]] = True  # 로봇의 초기 위치 방문 체크

    dfs(n=init_n, curr_position=init_pos, probability=init_probability)
    print(total_probability)


if __name__ == "__main__":
    total_probability = 0
    main()
