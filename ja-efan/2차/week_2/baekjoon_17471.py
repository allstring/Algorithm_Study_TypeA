# 게리맨더링
# Gold III

from collections import deque

"""
풀이 설명: 
    DFS로 각 구역이 어떤 선거구에 들어갈지 선택한다.  (combination 해도 됐을 듯)
    모든 구역의 선거구가 정해지면, 문제에서 주어진 선거구역 조건을 만족하는지 확인한다.
    (선거구는 하나 이상의 구역을 포함하고, 한 선거구에 포함된 구역은 모두 연결되어 있어야 한다. -> BFS) 
"""


def check_possibility(area_assignment):
    """
    나뉘어진 선거구가 유효한지 확인하는 함수
    """
    election_area_1 = [i for i in range(len(area_assignment)) if area_assignment[i] == 1]  # 1번 선거구에 포함된 구역
    election_area_2 = [i for i in range(len(area_assignment)) if area_assignment[i] == 2]  # 2번 선거구에 포함된 구역


    # 하나의 선거구에 몰린 경우 -> 불가능한 경우
    if len(election_area_1) == N or len(election_area_2) == N:
        return False

    # 1번 선거구가 모두 연결되어 있는지 확인 (BFS)
    src_area = election_area_1[0]
    visited_1 = set()
    visited_1.add(src_area)
    stack = deque([src_area])
    while stack:
        area = stack.popleft()
        for adj_area in adj_list[area]:
            if adj_area not in visited_1 and adj_area in election_area_1:
                visited_1.add(adj_area)
                stack.append(adj_area)

    # 방문한 구역의 개수가 선거구에 포함된 구역의 개수와 다른 경우
    if len(visited_1) != len(election_area_1):
        return False

    # 2번 선거구가 모두 연결되어 있는지 확인 (BFS)
    src_area = election_area_2[0]
    visited_2 = set()
    visited_2.add(src_area)
    stack = deque([src_area])
    while stack:
        area = stack.popleft()
        for adj_area in adj_list[area]:
            if adj_area not in visited_2 and adj_area in election_area_2:
                visited_2.add(adj_area)
                stack.append(adj_area)

    # 방문한 구역의 개수가 선거구에 포함된 구역의 개수와 다른 경우
    if len(visited_2) != len(election_area_2):
        return False

    return True


def dfs(curr_area, area_count, area_assignment):
    global min_diff
    # 선거구 유효성 확인 (모든 구역의 선거구가 정해진 경우)
    if area_count == N:
        if not check_possibility(area_assignment=area_assignment):
            return

        # 각 선거구에 포함된 구역들
        election_area_1 = [i for i in range(len(area_assignment)) if area_assignment[i] == 1]
        election_area_2 = [i for i in range(len(area_assignment)) if area_assignment[i] == 2]

        # 1번 선거구 내 인구수
        election_area_1_population = sum([population_list[area] for area in election_area_1])

        # 2번 선거구 내 인구수
        election_area_2_population = sum([population_list[area] for area in election_area_2])

        # 두 선거구의 인구수 차이
        diff = abs(election_area_2_population - election_area_1_population)
        # 최소 차이 갱신
        min_diff = min(min_diff, diff)

        return



    for election_area in range(1, 3):
        area_assignment[curr_area] = election_area
        dfs(curr_area=curr_area+1, area_count=area_count+1, area_assignment=area_assignment)


def main():
    global N, visited, adj_list, population_list
    N = int(input())
    population_list.extend(list(map(int, input().split())))
    visited = [False for _ in range(N+1)]
    for area in range(1, N+1):
        area_info = list(map(int, input().split()))
        # number_of_adj_area = area_info[0]
        adj_list[area] = area_info[1:]

    init_area = 1
    init_election_area = [0 for _ in range(N+1)]
    visited[init_area] = True
    dfs(init_area, 0, init_election_area)

    # 결과 출력
    if min_diff == 10000:
        print(-1)
        return
    print(min_diff)
    return

if __name__ == "__main__":
    min_diff = 10000
    population_list = [0]
    adj_list = dict()
    N = 0
    visited = list()
    main()